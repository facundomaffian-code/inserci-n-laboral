from flask import Flask, jsonify
from flask_cors import CORS
import json, os

app = Flask(__name__)
CORS(app)

DATA_FILE = os.path.join(os.path.dirname(__file__), 'careers_data.json')
with open(DATA_FILE, 'r', encoding='utf-8') as f:
    data = json.load(f)

@app.route('/api/careers')
def careers():
    return jsonify(data)

@app.route('/api/search')
def search():
    from flask import request
    q = request.args.get('q','').lower()
    results = [c for c in data if q in c['carrera'].lower()]
    return jsonify(results)

if __name__ == '__main__':
    app.run(debug=True)
