import hashlib,hmac,json,requests



class ChangellyApi(object):

    def __init__(self,API_KEY,API_SECRET):
        self.api_url = 'https://api.changelly.com'
        self.apikey=API_KEY
        self.apisecret = API_SECRET


    def api_call(self,identifier,type,**kwargs):

        print(type)
        message = {
            'jsonrpc': '2.0',
            'id': "{}".format(identifier),
            'method': type,
            'params': [kwargs]
        }

        serialized_data = json.dumps(message)

        sign = hmac.new(self.apisecret.encode('utf-8'), serialized_data.encode('utf-8'), hashlib.sha512).hexdigest()
        headers = {'api-key': self.apikey, 'sign': sign, 'Content-type': 'application/json'}

        response = requests.post(self.api_url, headers=headers, data=serialized_data)
        if response.ok:
            output=response.json()

        else:
            output=response.text

        return output


    def getCurrencies(self,id,**kwargs):
        '''Returns a list of enabled currencies as a flat array.'''

        call_type='getCurrencies'

        return self.api_call(id,call_type,**kwargs)


    def getCurrenciesFull(self,id,**kwargs):
        '''Returns a full list of currencies as an array of objects. Each object has an "enabled" field displaying current availability of a coin.'''

        call_type='getCurrenciesFull'

        return self.api_call(id,call_type,**kwargs)



    def getMinAmount(self,id,**kwargs):
        '''Returns a minimum allowed payin amount required for a currency pair. Amounts less than a minimal will most likely fail the transaction.'''

        call_type='getMinAmount'

        return self.api_call(id,call_type,**kwargs)


    def getExchangeAmount(self,id,**kwargs):
        '''Returns estimated exchange value with your API partner fee included.'''

        call_type="getExchangeAmount"

        return self.api_call(id,call_type,**kwargs)


    def generateAddress(self,id,**kwargs):
        '''Deprecated. Returns a pay-in address. A transaction ID will be generated later, while processing of the pay-in (when we will receive money).
         It’s better to use the "createTransaction" method instead, as "createTransaction" returns "transactionId" to monitor a transaction status.'''

        call_type='generateAddress'

        return self.api_call(id,call_type,**kwargs)


    def validateAddress(self,id,**kwargs):
        '''Returns if a given address is valid or not for a given currency.'''

        call_type="validateAddress"

        return self.api_call(id,call_type,**kwargs)


    def createTransaction(self,id,**kwargs):
        '''Creates a new transaction, generates a pay-in address and returns Transaction object with an ID field to track a transaction status.'''

        call_type="createTransaction"

        return self.api_call(id,call_type,**kwargs)


    def getStatus(self,id,**kwargs):
        '''Returns status of a given transaction using a transaction ID provided.'''

        call_type='getStatus'

        return self.api_call(id,call_type,**kwargs)



    def getTransactions(self,id,**kwargs):
        '''Returns an array of all transactions or a filtered list of transactions.'''

        call_type='getTransactions'

        return self.api_call(id,call_type,**kwargs)



