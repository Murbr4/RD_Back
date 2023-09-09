import json

from features.Service import Services

class cep(Services):
    def __init__(self, context):
        Services.__init__(self, context)

    def get_cep(self,cep):

        url_token = "https://viacep.com.br/ws/"+ cep + "/json/"

        data = Services.get_response(self, url_token)

        if data.status_code == 200:
            response = json.loads(data.text)

            if not response['logradouro']:
                return None
            if not response['ddd']:
                return None

            return response

