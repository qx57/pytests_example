from dto.pet import Pet
from test_data import common
import json
from dto.pet_change import PetChange

pet_file = "../resources/pet.json"
pet = Pet(pet_file, 'file')
with open(common.env_file) as json_file:
    env = json.load(json_file)

get_negative_params = [(pet.id, 'wrong_api_key', 403),
                       ('ololo', env[common.default_env]['api_key'], 400),
                       (1366, env[common.default_env]['api_key'], 404)]

pet_changes = [PetChange('../resources/pet_change1.json'),
               PetChange('../resources/pet_change2.json'),
               PetChange('../resources/pet_change3.json')]