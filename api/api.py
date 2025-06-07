from flask import Flask, jsonify
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

# Dados para o scraping
LOGIN_URL = 'https://sasweb.sascar.com.br/unificadoweb/site/login'
LOGIN_DATA_1 = {'username': 'INCOBEL262', 'password': 'incobel2012'}
LOGIN_DATA_2 = {'username': 'beve', 'password': 'tbeve2012'}

# Função para fazer login e coletar dados
def login_sascar(login_data):
    session = requests.Session()
    response = session.post(LOGIN_URL, data=login_data)
    return session if response.status_code == 200 else None

@app.route('/localizacoes', methods=['GET'])
def localizacoes():
    session_1 = login_sascar(LOGIN_DATA_1)
    session_2 = login_sascar(LOGIN_DATA_2)

    if not session_1 or not session_2:
        return jsonify({"error": "Erro ao autenticar na plataforma Sascar"}), 401

    # A URL para pegar as localizações dos caminhões
    # A URL e a lógica de scraping devem ser ajustadas de acordo com a estrutura real da plataforma Sascar
    localizacoes = []

    # Exemplo fictício de dados
    localizacoes.append({
        "placa": "RLO3J98", "latitude": -23.5505, "longitude": -46.6333,
        "data": "2022-06-01", "hora": "12:00", "velocidade": "60km/h", "ignicao": "ligada"
    })

    return jsonify(localizacoes)

if __name__ == '__main__':
    app.run(debug=True)
