import pytest
from api_entities.api_pet import ApiPet
from test_data import pet_by_id
from dto.pet import Pet

@pytest.fixture(scope='class',autouse=True)
def preparePet():
    # Create new pet
    response = ApiPet().post(pet_by_id.pet)
    if response.status_code == 200:
        pet_by_id.pet.id = response.json()["id"]
    else:
        raise Exception("Test pet not been defined!")

@pytest.fixture()
def petForDelete():
    response = ApiPet().post(pet_by_id.pet)
    if response.status_code != 200:
        raise Exception("Test pet not been defined!")
    return Pet(response.json(), 'json')