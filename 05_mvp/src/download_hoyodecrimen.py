import csv
import json
import time
from pathlib import Path

import requests
import urllib3
from shapely.geometry import Point, shape

API = "https://api.hoyodecrimen.com/api/v1"
CRIMES = ["ROBO A TRANSEUNTE C.V.", "ROBO A TRANSEUNTE S.V."]
MUNICIPIO = "CUAUHTEMOC"
START_DATE = "2019-01"
END_DATE = "2026-09"
RADIUS_M = 6000
PAUSE_S = 2
DATA_DIR = Path(__file__).resolve().parent.parent / "data"

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
headers = {"User-Agent": "research-client"}

response = requests.get(API + "/municipios/geojson", headers=headers, verify=False, timeout=120)
response.raise_for_status()
boundary_feature = None
for feature in response.json()["features"]:
    if feature["properties"]["municipio"] == MUNICIPIO:
        boundary_feature = feature
assert boundary_feature is not None, "municipio not found"
boundary = shape(boundary_feature["geometry"])

DATA_DIR.mkdir(exist_ok=True)
with open(DATA_DIR / "cuauhtemoc.geojson", "w", encoding="utf-8") as f:
    json.dump({"type": "FeatureCollection", "features": [boundary_feature]}, f, ensure_ascii=False)

center = boundary.envelope.centroid
victims = {}
for crime in CRIMES:
    time.sleep(PAUSE_S)
    url = API + "/latlong/crimes/" + crime + "/coords/" + str(center.x) + "/" + str(center.y) + "/distance/" + str(RADIUS_M)
    response = requests.get(url, params={"start_date": START_DATE, "end_date": END_DATE}, headers=headers, verify=False, timeout=300)
    response.raise_for_status()
    rows = response.json()["rows"]
    print(crime, len(rows), "filas descargadas")
    for row in rows:
        if not boundary.contains(Point(row["long"], row["lat"])):
            continue
        key = (row["date"], row["hour"], row["crime"], row["lat"], row["long"])
        if key in victims:
            victims[key] += 1
        else:
            victims[key] = 1

with open(DATA_DIR / "incidentes_cuauhtemoc.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["delito", "fecha", "hora", "lat", "lon", "victimas"])
    for key in sorted(victims):
        writer.writerow([key[2], key[0], key[1], key[3], key[4], victims[key]])

print(len(victims), "incidentes dentro de", MUNICIPIO)
