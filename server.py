from http.server import BaseHTTPRequestHandler, HTTPServer
import urllib.parse as urlparse
from urllib.parse import parse_qs
import joblib

model = joblib.load("fish.pkl")  # Load the model

class RequestHandler(BaseHTTPRequestHandler):
    def _send_response(self, message):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(bytes(message, "utf8"))
    def do_GET(self):
        query = urlparse.urlparse(self.path).query
        query_components = parse_qs(query)
        # Extract all inputs
        Length1 = float(query_components.get("Length1", [0])[0])
        Length2 = float(query_components.get("Length2", [0])[0])
        Length3 = float(query_components.get("Length3", [0])[0])
        Height = float(query_components.get("Height", [0])[0])
        Width = float(query_components.get("Width", [0])[0])
        species = query_components.get("species", ["Species_Bream"])[0]
        Species_Bream = 1 if species == "Species_Bream" else 0
        Species_Parkki = 1 if species == "Species_Parkki" else 0
        Species_Perch = 1 if species == "Species_Perch" else 0
        Species_Pike = 1 if species == "Species_Pike" else 0
        Species_Roach = 1 if species == "Species_Roach" else 0
        Species_Smelt = 1 if species == "Species_Smelt" else 0
        Species_Whitefish = 1 if species == "Species_Whitefish" else 0
        
        # Make prediction using model
        prediction = model.predict([[Length1, Length2, Length3, Height, Width, Species_Bream, Species_Parkki, Species_Perch, Species_Pike, Species_Roach, Species_Smelt, Species_Whitefish]])
        self._send_response(str(prediction))

def run():
    print('starting server...')
    server_address = ('127.0.0.1', 8080)
    httpd = HTTPServer(server_address, RequestHandler)
    print('running server...')
    httpd.serve_forever()

run()
