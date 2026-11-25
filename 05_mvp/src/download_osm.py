import json
from pathlib import Path

import osmnx as ox
from shapely.geometry import shape

NETWORK_TYPE = "walk"
DATA_DIR = Path(__file__).resolve().parent.parent / "data"

with open(DATA_DIR / "cuauhtemoc.geojson", encoding="utf-8") as f:
    boundary = shape(json.load(f)["features"][0]["geometry"])

ox.settings.use_cache = False
graph = ox.graph_from_polygon(boundary, network_type=NETWORK_TYPE, retain_all=False)
ox.save_graphml(graph, DATA_DIR / "red_peatonal_cuauhtemoc.graphml")

print(graph.number_of_nodes(), "nodos", graph.number_of_edges(), "aristas")
