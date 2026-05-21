"""
Serveur local pour la simulation pédagogique du devoir phishing.
Enregistre les identifiants fictifs dans captures.json sur cette machine uniquement.
"""

from http.server import HTTPServer, SimpleHTTPRequestHandler
import json
import os
from pathlib import Path

PORT = 8765
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

    def do_POST(self):
        if self.path != "/api/enregistrer":
            self.send_error(404, "Route introuvable")
            return

        length = int(self.headers.get("Content-Length", 0))
        raw_body = self.rfile.read(length)

        try:
            payload = json.loads(raw_body.decode("utf-8"))
        except json.JSONDecodeError:
            self.send_error(400, "JSON invalide")
            return

        email = str(payload.get("email", "")).strip()
        password = str(payload.get("password", "")).strip()

        if not email or not password:
            self.send_error(400, "E-mail et mot de passe requis")
            return

        entry = {
            "email": email,
            "password": password,
            "date": payload.get("date"),
        }

        captures = []
        if CAPTURES_FILE.exists():
            with CAPTURES_FILE.open("r", encoding="utf-8") as file:
                captures = json.load(file)

        captures.append(entry)

        with CAPTURES_FILE.open("w", encoding="utf-8") as file:
            json.dump(captures, file, indent=2, ensure_ascii=False)

        response = json.dumps({"ok": True, "message": "Enregistrement local effectué"}).encode(
            "utf-8"
        )

        self.send_response(200)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(response)))
        self.end_headers()
        self.wfile.write(response)

    def log_message(self, format, *args):
        print(f"[{self.log_date_time_string()}] {format % args}")


def main():
    os.chdir(ROOT)
    server = HTTPServer(("localhost", PORT), SimulationHandler)
    print(f"Serveur de simulation démarré : http://localhost:{PORT}")
    print(f"Ouvrir : http://localhost:{PORT}/login-simulation.html")
    print("Arrêt : Ctrl+C")
    server.serve_forever()


if __name__ == "__main__":
    main()
