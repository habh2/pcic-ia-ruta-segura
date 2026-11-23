import csv
import re
import threading
from datetime import datetime, timezone
from pathlib import Path

from flask import Flask, jsonify, request, send_from_directory

HOST = "127.0.0.1"
PORT = 8000
LANDING_DIR = Path(__file__).resolve().parent
DATA_FILE = LANDING_DIR / "data" / "preregistros.csv"
EMAIL_PATTERN = re.compile(r"^[^@\s]+@[^@\s]+\.[^@\s]+$")
MAX_EMAIL_LENGTH = 254

app = Flask(__name__)
lock = threading.Lock()


def read_emails():
    emails = set()
    if not DATA_FILE.exists():
        return emails
    with open(DATA_FILE, newline="", encoding="utf-8") as f:
        for row in csv.DictReader(f):
            emails.add(row["correo"])
    return emails


@app.post("/api/preregistro")
def preregister():
    body = request.get_json(silent=True)
    if body is None:
        body = {}
    email = str(body.get("email", "")).strip().lower()
    if len(email) > MAX_EMAIL_LENGTH or not EMAIL_PATTERN.match(email):
        return jsonify(ok=False, error="correo_invalido"), 400
    with lock:
        if email in read_emails():
            return jsonify(ok=True, duplicate=True)
        DATA_FILE.parent.mkdir(parents=True, exist_ok=True)
        is_new_file = not DATA_FILE.exists()
        with open(DATA_FILE, "a", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            if is_new_file:
                writer.writerow(["fecha_utc", "correo"])
            writer.writerow([datetime.now(timezone.utc).isoformat(timespec="seconds"), email])
    return jsonify(ok=True, duplicate=False)


@app.get("/")
def index():
    return send_from_directory(LANDING_DIR, "index.html")


@app.get("/assets/<path:name>")
def assets(name):
    return send_from_directory(LANDING_DIR / "assets", name)


app.run(host=HOST, port=PORT)
