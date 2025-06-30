import requests
import json

def get_bitcoin_price():
    try:
        response = requests.get('https://economia.awesomeapi.com.br/json/last/BTC-BRL')
        response.raise_for_status()  # Lança um erro para respostas ruins (4xx ou 5xx)
        data = response.json()
        # A estrutura da Awesome API é { "BTCBRL": { ... } }
        price = data['BTCBRL']['bid']
        print(f"Olá! A cotação atual do Bitcoin é R$ {price}")
    except requests.exceptions.RequestException as e:
        print(f"Erro ao buscar a cotação: {e}")
    except KeyError:
        print("Não foi possível encontrar a cotação do Bitcoin na resposta da API.")

if __name__ == "__main__":
    get_bitcoin_price()