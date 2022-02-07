class Category:
    def __init__(self, pet_json):
        self.id = pet_json["id"]
        self.name = pet_json["name"]

    def __eq__(self, other):
        if isinstance(other, Category):
            return (self.id == other.id and self.name == other.name)
        return NotImplemented