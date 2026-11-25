import csv
import heapq
import json
import math
from pathlib import Path

import geopandas as gpd
import numpy as np
import osmnx as ox
import pandas as pd
from shapely import STRtree
from shapely.geometry import LineString, Point
from sklearn.neighbors import KernelDensity

FIT_YEARS = [2021, 2022, 2023, 2024]
VALIDATION_YEAR = 2025
TEST_YEAR = 2026
BANDWIDTHS_M = [25, 50, 75, 100, 150, 200, 300, 400]
SAMPLE_STEP_M = 10
SEEDS = [0, 1, 2, 3, 4]
RANDOM_PAIRS = 200
ZONE_PAIRS = 50
MIN_PAIR_M = 1000
MAX_PAIR_M = 4000
WALK_SPEED_MPS = 1.4
EPSILONS = [0.1, 0.2]
LAMBDA_MIN = 0.01
LAMBDA_MAX = 10000.0
LAMBDA_STEPS = 16
EXPOSURE_RADIUS_M = 50
HIGH_ZONE = (19.43412, -99.14081)
LOW_ZONE = (19.40983, -99.15768)
ZONE_REPORTS = 15
ZONE_SPREAD_M = 60
ZONE_RADIUS_M = 150
FAKE_REPORTS = 30
REPORT_PEAK_PERCENTILE = 90
COMMUNITY_SEED = 0
COMMUNITY_MAX_AGE_DAYS = 45
APP_REPORT_TYPES = ["luz", "robo", "acoso", "sola", "banqueta"]
EARTH_RADIUS_M = 6371009
CRS = "EPSG:32614"
ROOT = Path(__file__).resolve().parent.parent
DATA_DIR = ROOT / "data"
RESULTS_DIR = ROOT / "resultados"
APP_DATA_DIR = ROOT / "web" / "assets" / "data"

graph = ox.load_graphml(DATA_DIR / "red_peatonal_cuauhtemoc.graphml")
edges = ox.graph_to_gdfs(ox.project_graph(graph, to_crs=CRS), nodes=False)
lengths = edges["length"].values

incidents = pd.read_csv(DATA_DIR / "incidentes_cuauhtemoc.csv")
incidents["anio"] = incidents["fecha"].str[:4].astype(int)
points = gpd.GeoSeries(gpd.points_from_xy(incidents["lon"], incidents["lat"]), crs="EPSG:4326").to_crs(CRS)
incidents["x"] = points.x.values
incidents["y"] = points.y.values
fit_xy = incidents[incidents["anio"].isin(FIT_YEARS)][["x", "y"]].values
validation_xy = incidents[incidents["anio"] == VALIDATION_YEAR][["x", "y"]].values
test_xy = incidents[incidents["anio"] == TEST_YEAR][["x", "y"]].values
print(len(fit_xy), "incidentes de ajuste,", len(validation_xy), "de validacion,", len(test_xy), "de prueba")

RESULTS_DIR.mkdir(exist_ok=True)
bandwidth = None
best_score = -math.inf
with open(RESULTS_DIR / "seleccion_ancho.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["ancho_m", "log_verosimilitud_media"])
    for candidate in BANDWIDTHS_M:
        score = KernelDensity(kernel="gaussian", bandwidth=candidate).fit(fit_xy).score_samples(validation_xy).mean()
        writer.writerow([candidate, round(score, 4)])
        if score > best_score:
            best_score = score
            bandwidth = candidate
print("ancho elegido", bandwidth, "m")

sample_x = []
sample_y = []
sample_edge = []
for i, line in enumerate(edges.geometry.values):
    count = max(2, math.ceil(line.length / SAMPLE_STEP_M) + 1)
    for distance in np.linspace(0, line.length, count):
        point = line.interpolate(distance)
        sample_x.append(point.x)
        sample_y.append(point.y)
        sample_edge.append(i)
sample_xy = np.column_stack([sample_x, sample_y])
sample_edge = np.array(sample_edge)
samples_per_edge = np.bincount(sample_edge)

kde = KernelDensity(kernel="gaussian", bandwidth=bandwidth).fit(fit_xy)
edge_density = np.bincount(sample_edge, weights=np.exp(kde.score_samples(sample_xy))) / samples_per_edge
base_risk = edge_density / ((lengths * edge_density).sum() / lengths.sum())
report_peak = np.percentile(base_risk, REPORT_PEAK_PERCENTILE)
print("riesgo base: mediana", round(float(np.median(base_risk)), 4), "maximo", round(base_risk.max(), 4), "altura de un reporte", round(report_peak, 4))

with open(RESULTS_DIR / "riesgo_aristas.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["u", "v", "key", "longitud_m", "densidad_por_m2", "riesgo"])
    for i, index in enumerate(edges.index):
        writer.writerow([index[0], index[1], index[2], round(lengths[i], 2), "%.6e" % edge_density[i], round(base_risk[i], 4)])

node_ids = list(graph.nodes)
index_of = {}
for i, node in enumerate(node_ids):
    index_of[node] = i
lat = np.radians(np.array([graph.nodes[n]["y"] for n in node_ids]))
lon = np.radians(np.array([graph.nodes[n]["x"] for n in node_ids]))
edge_tail = []
edge_head = []
for index in edges.index:
    edge_tail.append(index_of[index[0]])
    edge_head.append(index_of[index[1]])
edge_geometry = edges.geometry.values

latlon_edges = ox.graph_to_gdfs(graph, nodes=False).loc[edges.index]
names = []
name_index = {}
app_edges = []
app_geometries = []
for i in range(len(edges)):
    if edge_tail[i] >= edge_head[i]:
        continue
    name = latlon_edges["name"].values[i]
    if isinstance(name, list):
        name = name[0]
    if not isinstance(name, str):
        if latlon_edges["highway"].values[i] == "footway":
            name = "la banqueta"
        else:
            name = "una calle sin nombre"
    if name not in name_index:
        name_index[name] = len(names)
        names.append(name)
    geometry_index = -1
    coords = list(latlon_edges.geometry.values[i].coords)
    if len(coords) > 2:
        flat = []
        for x, y in coords[1:-1]:
            flat.append(round(y, 6))
            flat.append(round(x, 6))
        geometry_index = len(app_geometries)
        app_geometries.append(flat)
    app_edges.append([edge_tail[i], edge_head[i], round(float(lengths[i]), 1), round(float(base_risk[i]), 3), name_index[name], geometry_index])

app_nodes = []
for n in node_ids:
    app_nodes.append(round(graph.nodes[n]["y"], 6))
    app_nodes.append(round(graph.nodes[n]["x"], 6))
with open(DATA_DIR / "cuauhtemoc.geojson", encoding="utf-8") as f:
    boundary_coords = json.load(f)["features"][0]["geometry"]["coordinates"][0]
app_boundary = []
for x, y in boundary_coords:
    app_boundary.append([round(y, 5), round(x, 5)])

APP_DATA_DIR.mkdir(parents=True, exist_ok=True)
with open(APP_DATA_DIR / "red_cuauhtemoc.json", "w", encoding="utf-8") as f:
    json.dump({"speed_mps": WALK_SPEED_MPS, "bandwidth_m": bandwidth, "report_peak": round(float(report_peak), 4),
               "boundary": app_boundary, "nodes": app_nodes, "names": names, "edges": app_edges,
               "geometries": app_geometries}, f, ensure_ascii=False, separators=(",", ":"))
print(len(app_edges), "calles exportadas para la app")

zone_xy = gpd.GeoSeries([Point(HIGH_ZONE[1], HIGH_ZONE[0]), Point(LOW_ZONE[1], LOW_ZONE[0])], crs="EPSG:4326").to_crs(CRS)
high_center = np.array([zone_xy.x.values[0], zone_xy.y.values[0]])
low_center = np.array([zone_xy.x.values[1], zone_xy.y.values[1]])
test_tree = STRtree([Point(x, y) for x, y in test_xy])


def haversine_m(i, j):
    a = math.sin((lat[j] - lat[i]) / 2) ** 2 + math.cos(lat[i]) * math.cos(lat[j]) * math.sin((lon[j] - lon[i]) / 2) ** 2
    return 2 * EARTH_RADIUS_M * math.asin(math.sqrt(a))


def search(adjacency, start, goal, lam, use_heuristic):
    best = {start: 0.0}
    parent_edge = {start: None}
    closed = set()
    frontier = [(0.0, 0.0, start)]
    expanded = 0
    while frontier:
        f, g, node = heapq.heappop(frontier)
        if node in closed:
            continue
        closed.add(node)
        expanded += 1
        if node == goal:
            break
        for nxt, seconds, risk, edge in adjacency[node]:
            if nxt in closed:
                continue
            new_g = g + seconds * (1 + lam * risk)
            if nxt not in best or new_g < best[nxt]:
                best[nxt] = new_g
                parent_edge[nxt] = edge
                h = 0.0
                if use_heuristic:
                    h = haversine_m(nxt, goal) / WALK_SPEED_MPS
                heapq.heappush(frontier, (new_g + h, new_g, nxt))
    path = []
    node = goal
    while parent_edge[node] is not None:
        path.append(parent_edge[node])
        node = edge_tail[parent_edge[node]]
    path.reverse()
    return path, best[goal], expanded


def route_seconds(path):
    seconds = 0.0
    for edge in path:
        seconds += lengths[edge] / WALK_SPEED_MPS
    return seconds


def budget_route(adjacency, start, goal, budget):
    top_path, top_cost, top_expanded = search(adjacency, start, goal, LAMBDA_MAX, True)
    if route_seconds(top_path) <= budget:
        return LAMBDA_MAX
    bottom_path, bottom_cost, bottom_expanded = search(adjacency, start, goal, LAMBDA_MIN, True)
    if route_seconds(bottom_path) > budget:
        return 0.0
    low = math.log(LAMBDA_MIN)
    high = math.log(LAMBDA_MAX)
    for step in range(LAMBDA_STEPS):
        middle = (low + high) / 2
        middle_path, middle_cost, middle_expanded = search(adjacency, start, goal, math.exp(middle), True)
        if route_seconds(middle_path) <= budget:
            low = middle
        else:
            high = middle
    return math.exp(low)


def route_line(path):
    coords = []
    for edge in path:
        segment = list(edge_geometry[edge].coords)
        if coords:
            segment = segment[1:]
        coords.extend(segment)
    return LineString(coords)


def count_near(tree, path):
    return len(tree.query(route_line(path).buffer(EXPOSURE_RADIUS_M), predicate="contains"))


def distance_to_route(path, center):
    return route_line(path).distance(Point(center[0], center[1]))


base_adjacency = []
for i in range(len(node_ids)):
    base_adjacency.append([])
for i in range(len(edges)):
    base_adjacency[edge_tail[i]].append((edge_head[i], lengths[i] / WALK_SPEED_MPS, base_risk[i], i))

rows = []
report_rows = []
for seed in SEEDS:
    rng = np.random.default_rng(seed)

    high_reports = high_center + rng.normal(0, ZONE_SPREAD_M, (ZONE_REPORTS, 2))
    low_reports = low_center + rng.normal(0, ZONE_SPREAD_M, (ZONE_REPORTS, 2))
    fake_edges = rng.choice(len(edges), FAKE_REPORTS, p=lengths / lengths.sum())
    fake_reports = []
    for i in fake_edges:
        point = edges.geometry.values[i].interpolate(rng.random(), normalized=True)
        fake_reports.append([point.x, point.y])
    fake_reports = np.array(fake_reports)
    all_reports = np.vstack([high_reports, low_reports, fake_reports])
    kinds = ["zona_alta"] * ZONE_REPORTS + ["zona_baja"] * ZONE_REPORTS + ["falso"] * FAKE_REPORTS
    report_points = gpd.GeoSeries(gpd.points_from_xy(all_reports[:, 0], all_reports[:, 1]), crs=CRS).to_crs("EPSG:4326")
    for i in range(len(all_reports)):
        report_rows.append([seed, kinds[i], round(report_points.y.values[i], 6), round(report_points.x.values[i], 6)])

    report_kde = KernelDensity(kernel="gaussian", bandwidth=bandwidth).fit(all_reports)
    bump_sum = len(all_reports) * 2 * math.pi * bandwidth ** 2 * np.exp(report_kde.score_samples(sample_xy))
    report_risk = report_peak * np.bincount(sample_edge, weights=bump_sum) / samples_per_edge
    report_adjacency = []
    for i in range(len(node_ids)):
        report_adjacency.append([])
    for i in range(len(edges)):
        report_adjacency[edge_tail[i]].append((edge_head[i], lengths[i] / WALK_SPEED_MPS, base_risk[i] + report_risk[i], i))

    high_tree = STRtree([Point(x, y) for x, y in high_reports])
    low_tree = STRtree([Point(x, y) for x, y in low_reports])
    fake_tree = STRtree([Point(x, y) for x, y in fake_reports])

    pairs = []
    zone_counts = {"zona_alta": 0, "zona_baja": 0}
    random_count = 0
    while random_count < RANDOM_PAIRS or zone_counts["zona_alta"] < ZONE_PAIRS or zone_counts["zona_baja"] < ZONE_PAIRS:
        a = int(rng.integers(len(node_ids)))
        b = int(rng.integers(len(node_ids)))
        distance = haversine_m(a, b)
        if distance < MIN_PAIR_M or distance > MAX_PAIR_M:
            continue
        if random_count < RANDOM_PAIRS:
            pairs.append(("aleatorio", a, b))
            random_count += 1
            continue
        fast_path, fast_cost, fast_expanded = search(base_adjacency, a, b, 0.0, True)
        if zone_counts["zona_alta"] < ZONE_PAIRS and distance_to_route(fast_path, high_center) <= ZONE_RADIUS_M:
            pairs.append(("zona_alta", a, b))
            zone_counts["zona_alta"] += 1
        elif zone_counts["zona_baja"] < ZONE_PAIRS and distance_to_route(fast_path, low_center) <= ZONE_RADIUS_M:
            pairs.append(("zona_baja", a, b))
            zone_counts["zona_baja"] += 1

    for pair_number, (pair_set, start, goal) in enumerate(pairs):
        fast_path, fast_cost, fast_expanded = search(base_adjacency, start, goal, 0.0, True)
        ucs_path, ucs_cost, ucs_expanded = search(base_adjacency, start, goal, 0.0, False)
        assert abs(fast_cost - ucs_cost) < 1e-6, "A* and uniform-cost search disagree"
        fast_seconds = route_seconds(fast_path)
        candidates = [("base", 0.0, fast_path, fast_expanded, ucs_expanded)]
        for epsilon in EPSILONS:
            budget = (1 + epsilon) * fast_seconds
            for name, adjacency in [("riesgo", base_adjacency), ("riesgo_reportes", report_adjacency)]:
                lam = budget_route(adjacency, start, goal, budget)
                path, cost, expanded = search(adjacency, start, goal, lam, True)
                ucs_path, ucs_cost, ucs_expanded = search(adjacency, start, goal, lam, False)
                assert abs(cost - ucs_cost) < 1e-6, "A* and uniform-cost search disagree"
                assert route_seconds(path) <= budget + 1e-6, "route exceeds the time budget"
                candidates.append((name + "_eps_" + str(epsilon), lam, path, expanded, ucs_expanded))
        for name, lam, path, expanded, ucs_expanded in candidates:
            seconds = route_seconds(path)
            rows.append([seed, pair_number, pair_set, node_ids[start], node_ids[goal], name, lam, seconds,
                         100 * (seconds / fast_seconds - 1), seconds * WALK_SPEED_MPS / 1000,
                         count_near(test_tree, path), count_near(high_tree, path), count_near(low_tree, path),
                         count_near(fake_tree, path), expanded, ucs_expanded])
    print("semilla", seed, "terminada")

with open(RESULTS_DIR / "reportes_sinteticos.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["semilla", "tipo", "lat", "lon"])
    writer.writerows(report_rows)

community_rng = np.random.default_rng(COMMUNITY_SEED)
community = []
for seed, kind, report_lat, report_lon in report_rows:
    if seed != COMMUNITY_SEED:
        continue
    report_type = APP_REPORT_TYPES[int(community_rng.integers(len(APP_REPORT_TYPES)))]
    age_days = int(community_rng.integers(COMMUNITY_MAX_AGE_DAYS))
    community.append({"lat": report_lat, "lon": report_lon, "tipo": report_type, "edad_dias": age_days})
with open(APP_DATA_DIR / "reportes_comunidad.json", "w", encoding="utf-8") as f:
    json.dump(community, f, ensure_ascii=False, separators=(",", ":"))

table = pd.DataFrame(rows, columns=["semilla", "par", "conjunto", "origen", "destino", "metodo", "lambda", "tiempo_s",
                                    "sobrecosto_tiempo_pct", "longitud_km", "incidentes_prueba", "reportes_zona_alta",
                                    "reportes_zona_baja", "reportes_falsos", "nodos_astar", "nodos_costo_uniforme"])
table.to_csv(RESULTS_DIR / "rutas.csv", index=False)

measures = ["incidentes_prueba", "reportes_zona_alta", "reportes_zona_baja", "reportes_falsos", "sobrecosto_tiempo_pct", "nodos_astar", "nodos_costo_uniforme"]
per_seed = table.groupby(["conjunto", "metodo", "semilla"])[measures].mean()
summary = per_seed.groupby(["conjunto", "metodo"]).agg(["mean", "std"])
summary.columns = [name + "_" + stat.replace("mean", "media").replace("std", "desv") for name, stat in summary.columns]
summary.to_csv(RESULTS_DIR / "resumen.csv")
print(summary.round(2).to_string())
