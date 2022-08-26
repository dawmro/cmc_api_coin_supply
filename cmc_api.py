
from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import secrets


class CMC:
    # https://coinmarketcap.com/api/documentation/v1/#
    def __init__(self, token):
        self.api_url = 'https://pro-api.coinmarketcap.com'
        self.headers = {
            'Accepts': 'application/json',
            'X-CMC_PRO_API_KEY': token,
        }
        self.session = Session()
        self.session.headers.update(self.headers)
        
            
    def getPrice(self, symbol):
        url = self.api_url + '/v1/cryptocurrency/quotes/latest'
        parameters = {'symbol': symbol}
        try:
            r = self.session.get(url, params = parameters)
            data = r.json()['data']
            return data
        except (ConnectionError, Timeout, TooManyRedirects) as e:
            print(e)
        


if __name__ == '__main__':

    cmc = CMC(secrets.API_KEY)
    
    btc_total_supply = cmc.getPrice('BTC')['BTC']['total_supply']
    btc_max_supply = cmc.getPrice('BTC')['BTC']['max_supply']
    
    
    print(f"How much of BTC has been mined already: {btc_total_supply} of: {btc_max_supply}")

