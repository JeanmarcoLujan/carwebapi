class Vehicle:
    def __init__(self, id, brand, model):
        self.id = id
        self.brand = brand
        self.model = model

    def to_json(self):
        return {'id': self.id, 'brand': self.brand, 'model': self.model}