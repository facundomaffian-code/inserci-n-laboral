from flask import Flask, jsonify, send_from_directory, request
from flask_cors import CORS
import json, os

# Flask configurado para servir archivos desde la raíz
app = Flask(__name__, static_folder='.', static_url_path='')
CORS(app)

# Cargar datos del JSON
DATA_FILE = os.path.join(os.path.dirname(__file__), 'careers_data.json')
with open(DATA_FILE, 'r', encoding='utf-8') as f:
    data = json.load(f)

# -----------------------------
#          API ROUTES
# -----------------------------
@app.route('/api/careers')
def careers():
    return jsonify(data)

@app.route('/api/search')
def search():
    q = request.args.get('q', '').lower()
    results = [c for c in data if q in c['carrera'].lower()]
    return jsonify(results)

# -----------------------------
#       RUTA PRINCIPAL
#  SIRVE EL INDEX.HTML NUEVO
# -----------------------------
@app.route('/')
def index():
    return send_from_directory('.', 'index.html')

# -----------------------------
#   SERVIR CUALQUIER ARCHIVO
#    CSS / JS / IMÁGENES, ETC
# -----------------------------
@app.route('/<path:path>')
def static_files(path):
    return send_from_directory('.', path)

# -----------------------------
#  CONFIG ESPECIAL PARA RENDER
# -----------------------------
if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
