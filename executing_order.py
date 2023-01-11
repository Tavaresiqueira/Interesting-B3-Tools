import requests
import json

access_token = "SEU ACCESS TOKEN"
headers = {'Authorization': 'Bearer ' + access_token}

# Define a URL da API da clear
url = 'https://api.clear.com.br/order'

# dados de compra ou venda
data = {
    "account": "nº da conta",
    "symbol": "PETR4",
    "side": "buy",
    "type": "limit",
    "timeInForce": "day",
    "price": "15.00",
    "quantity": "100"
}

# Faz a requisição POST na url da clear
response = requests.post(url, headers=headers, json=data)

# Verifica se a requisição foi bem-sucedida
if response.status_code == 201:
    print('Ordem enviada com sucesso!')
    print(response.json())
else:
    print('Falha ao enviar ordem')