import pytest
from test_data import pet_by_id
from dto.pet import Pet
from api_entities.api_get_pet import ApiPetById

class TestPetById:
    @pytest.mark.somemark
    @pytest.mark.positive
    def test_get_pet_positive(self):
        response = ApiPetById().get(pet_by_id.pet.id)
        assert response.status_code == 200
        assert Pet(response.json(), 'json') == pet_by_id.pet

    @pytest.mark.somemark
    @pytest.mark.negative
    @pytest.mark.parametrize('pet_id, api_key, response_code', pet_by_id.get_negative_params)
    def test_get_pet_negatives(self, pet_id, api_key, response_code):
        response = ApiPetById().getWithKey(pet_id, api_key)
        assert response.status_code == response_code

    @pytest.mark.somemark
    @pytest.mark.positive
    def test_update_pet_positive(self):
        response = ApiPetById().post(pet_by_id.pet.id, 'Oliver', 'sold')
        assert response.status_code == 200

    @pytest.mark.somemark
    @pytest.mark.negative
    @pytest.mark.parametrize('curr_pet', pet_by_id.pet_changes)
    def test_update_pet_negative(self, curr_pet):
        curr_id = pet_by_id.pet.id if curr_pet.id == None else curr_pet.id
        response = ApiPetById().postWithKey(curr_id, curr_pet.key, curr_pet.name, curr_pet.status)
        assert response.status_code == curr_pet.response_code

    @pytest.mark.somemark
    @pytest.mark.positive
    def test_delete_pet_positive(self, petForDelete):
        response = ApiPetById().delete(petForDelete.id)
        assert response.status_code == 200