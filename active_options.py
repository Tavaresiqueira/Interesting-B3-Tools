import requests
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry
import json

def get_options_quote(symbol):
    # sessao com retry para obter as opcoes em aberto de determinado ativo da B3
    session = requests.Session()
    retry = Retry(total=3,
                  read=3,
                  connect=3,
                  backoff_factor=0.5,
                  status_forcelist=[429, 500, 502, 503, 504])
    adapter = HTTPAdapter(max_retries=retry)
    session.mount('https://', adapter)
    
    # solicitacao por meio de um metodo get
    response = session.get(f"https://api.bmfbovespa.com.br/api/v1/opcoes/acoes/{symbol}")

    if response.status_code == 200:
        data = json.loads(response.text)

    return data