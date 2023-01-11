import requests
import json

def get_financial_statements(symbol):
    # Faz uma solicitacao a Api da b3
    # lembrando que para executar isso ha necessidade de se ter um acesso de developer da B3
    response = requests.get(f"https://api.bmfbovespa.com.br/api/v1/balancos/{symbol}")

    # retornando os detalhes dos financial statements
    if response.status_code == 200:
        data = json.loads(response.text)

        financial_statements = data["financial_statements"]

        return financial_statements
    else:
        return None
        