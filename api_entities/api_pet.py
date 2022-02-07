import requests
from test_data import common
import json

class ApiPet:
    def __init__(self):
        self.response = None
        self.env = common.default_env
        with open(common.env_file) as json_file:
            json_env = json.load(json_file)
        self.base_url = json_env[self.env]['base_url']
        self.path = json_env[self.env]['path']['pet']
        self.api_key = json_env[self.env]['api_key']

    def post(self, pet):
        json_body = json.dumps(pet, default=lambda x: x.__dict__)
        response = requests.post(self.base_url + self.path,
                      data = json_body,
                      headers = {
                          'content-type': 'application/json',
                          'api_key': self.api_key})
        return response