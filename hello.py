import requests
import argparse

def get_crypto_price(crypto_symbol='BTC'):
    """
    Busca o preço de uma criptomoeda em BRL na Awesome API.
    """
    api_url = f'https://economia.awesomeapi.com.br/json/last/{crypto_symbol}-BRL'
    try:
        response = requests.get(api_url)
        response.raise_for_status()  # Lança um erro para respostas ruins (4xx ou 5xx)
        data = response.json()
        
        # A chave do dicionário é dinâmica (ex: 'BTCBRL', 'ETHBRL')
        data_key = f"{crypto_symbol}BRL"
        if data_key not in data:
            # A API retorna 404 para símbolos inválidos, mas verificamos por segurança
            print(f"Erro: Símbolo de criptomoeda '{crypto_symbol}' não encontrado na API.")
            return

        price = data[data_key]['bid']
        name = data[data_key]['name']
        
        print(f"A cotação atual do {name} é R$ {price}")

    except requests.exceptions.HTTPError as http_err:
        if http_err.response.status_code == 404:
            print(f"Erro: Não foi possível encontrar a cotação para o símbolo '{crypto_symbol}'. Verifique se o símbolo está correto.")
        else:
            print(f"Erro HTTP ao buscar a cotação: {http_err}")
    except requests.exceptions.RequestException as e:
        print(f"Erro de conexão ao buscar a cotação: {e}")
    except KeyError:
        print(f"Não foi possível encontrar a cotação de '{crypto_symbol}' na resposta da API.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Busca a cotação de uma criptomoeda em Reais (BRL)."
    )
    parser.add_argument(
        'simbolo', 
        type=str, 
        nargs='?', 
        default='BTC',
        help="O símbolo da criptomoeda a ser buscada (ex: ETH, LTC). Padrão é BTC."
    )
    args = parser.parse_args()
    
    get_crypto_price(args.simbolo.upper())
