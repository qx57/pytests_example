import json
from test_data import common

class PetChange:
    def __init__(self, file):
        with open(common.env_file) as json_file:
            env = json.load(json_file)
        with open(file) as json_file:
            pc_json = json.load(json_file)
        self.id = pc_json['id']
        self.key = env[common.default_env]['api_key'] if ('key' not in pc_json or pc_json['key'] == None) \
            else pc_json['key']
        self.name = pc_json['name']
        self.status = pc_json['status']
        self.response_code = pc_json['response_code']