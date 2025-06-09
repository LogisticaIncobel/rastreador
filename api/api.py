import requests
import json
import os

LOGIN_URL = 'https://sasweb.sascar.com.br/unificadoweb/site/login'
LOGIN_DATA_1 = {'username': 'INCOBEL262', 'password': 'incobel2012'}
LOGIN_DATA_2 = {'username': 'beve', 'password': 'tbeve2012'}

def login_sascar(login_data):
    session = requests.Session()
    response = session.post(LOGIN_URL, data=login_data)
    return session if response.status_code == 200 else None

def coletar_dados():
    session_1 = login_sascar(LOGIN_DATA_1)
    session_2 = login_sascar(LOGIN_DATA_2)

    if not session_1 or not session_2:
        print("Erro ao autenticar na Sascar.")
        return

    localizacoes = [
        {
            "placa": "RLO3J98",
            "latitude": -23.5505,
            "longitude": -46.6333,
            "data": "2025-06-09",
            "hora": "12:00",
            "velocidade": "60km/h",
            "ignicao": "ligada"
        }
    ]

    os.makedirs("public", exist_ok=True)
    with open("public/localizacoes.json", "w", encoding="utf-8") as f:
        json.dump(localizacoes, f, ensure_ascii=False, indent=2)

if __name__ == "__main__":
    coletar_dados()
