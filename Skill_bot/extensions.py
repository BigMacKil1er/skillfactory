import requests
import json
from config import keys


class APIException(Exception):
    pass
class CryptoConverter:
    @staticmethod
    def get_price(quote: str, base: str, amount: str):
        
        if quote == base:
            raise APIException(f'Не возможно перевести одинаковые валюты {base}')

        try:
            quote_ticker = keys[quote]
        except KeyError:
            raise APIException(f'Не удалось обработать валюту {quote}')
        
        try:
            quote_ticker = keys[base]
        except KeyError:
            raise APIException(f'Не удалось обработать валюту {base}')

        try:
            amount =float(amount)
        except ValueError:
            raise APIException(f'Не удалось обработать количество {amount}')
        quote_ticker, base_ticker = keys[quote], keys[base]

        url = f"https://api.apilayer.com/exchangerates_data/convert?to={base_ticker}&from={quote_ticker}&amount={amount}"

        payload = {}
        headers = {
            "apikey": "E8VZDw6w4itc31XhK6rMkHpD3o3Z303Q"
        }

        response = requests.request("GET", url, headers=headers, data=payload)

        total_base = json.loads(response.content)['info']['rate']
        return total_base