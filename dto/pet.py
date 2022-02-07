import collections

from dto.category import Category
import json

class Pet:
    def __init__(self, data, type):
        pet_json = self.get_json(data, type)
        self.id = None if 'id' not in pet_json else pet_json['id']
        self.category = Category(pet_json['category'])
        self.name = pet_json['name']
        self.photoUrls = pet_json['photoUrls']
        self.tags = pet_json['tags']
        self.status = pet_json['status']

    def get_json(self, data, type):
        curr_json = None
        if type == 'file':
            with open(data) as json_file:
                curr_json = json.load(json_file)
        else:
            curr_json = data
        return curr_json

    def __eq__(self, other):
        if isinstance(other, Pet):
            return (self.id == other.id and
                    self.name == other.name and
                    self.status == other.status and
                    self.category == other.category and
                    collections.Counter(self.photoUrls) == collections.Counter(other.photoUrls) and
                    collections.Counter(self.tags) == collections.Counter(other.tags))
        return NotImplemented