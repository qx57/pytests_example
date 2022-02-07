import requests
from test_data import common
import json

class ApiPetById:
    def __init__(self):
        self.env = common.default_env
        with open(common.env_file) as json_file:
            json_env = json.load(json_file)
        self.base_url = json_env[self.env]['base_url']
        self.path = json_env[self.env]['path']['petId']
        self.api_key = json_env[self.env]['api_key']

    def get(self, id):
        return self.getWithKey(id, self.api_key)

    def getWithKey(self, custom_id, custom_key):
        return requests.get(self.getUrl(custom_id),
                            headers = {'api_key': custom_key})

    def post(self, id, name, status):
        return self.postWithKey(id, self.api_key, name, status)

    def postWithKey(self, custom_id, custom_key, name, status):
        return requests.post(self.getUrl(custom_id),
                             data = {
                                 'name': name,
                                 'status': status
                             },
                             headers = {
                                 'content-type': 'application/x-www-form-urlencoded',
                                 'api_key': custom_key
                             })

    def delete(self, id):
        return requests.delete(self.getUrl(id), headers = {'api_key': self.api_key})

    def getUrl(self, id):
        url = self.base_url + self.path
        return url.replace('{petId}', str(id))