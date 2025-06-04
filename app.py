from flask import Flask, jsonify, request
from flask_cors import CORS
import scraper  # Módulo que vamos criar para raspar os dados

app = Flask(__name__)
CORS(app)  # Habilita CORS para todas as rotas

# Rota principal
@app.route('/')
def home():
    return jsonify({
        "message": "API de dados da vitivinicultura - Embrapa",
        "endpoints": {
            "producao": "/api/producao",
            "processamento": "/api/processamento",
            "comercializacao": "/api/comercializacao",
            "importacao": "/api/importacao",
            "exportacao": "/api/exportacao"
        }
    })

# Rotas da API
@app.route('/api/producao')
def get_producao():
    data = scraper.get_data('opt_02')
    return jsonify(data)

@app.route('/api/processamento')
def get_processamento():
    data = scraper.get_data('opt_03')
    return jsonify(data)

@app.route('/api/comercializacao')
def get_comercializacao():
    data = scraper.get_data('opt_04')
    return jsonify(data)

@app.route('/api/importacao')
def get_importacao():
    data = scraper.get_data('opt_05')
    return jsonify(data)

@app.route('/api/exportacao')
def get_exportacao():
    data = scraper.get_data('opt_06')
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)