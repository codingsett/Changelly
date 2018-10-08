import requests_mock
from Changelly.changelly import ChangellyApi


apikey = 'test_api_key'
apisecret = 'test_api_secret'

api = ChangellyApi(apikey,apisecret)


def test_authorization():

    with requests_mock.mock() as sim:
        headers = {'api-key':apikey, 'sign': 'sign', 'Content-type': 'application/json'}
        sim.post('https://api.changelly.com',headers=headers,text="Unauthorized",status_code=401)
        api.getCurrencies("test")



def test_successfulapicall():

    with requests_mock.mock() as sim:
        headers = {'api-key':apikey, 'sign': 'sign', 'Content-type': 'application/json'}
        data={'jsonrpc': '2.0', 'id': 'test', 'result': ['btc', 'eth', 'etc', 'exp', 'xem', 'lsk', 'game', 'zec', 'nlg','eos', 'pay', 'bch', 'neo', 'omg', 'ignis']}

        sim.post('https://api.changelly.com',headers=headers,json=data,status_code=401)
        api.getCurrencies("test")

