import json
from dawai import Dawai

class DawaiInformation:
    def __init__(self, filepath='medicines.json'):
        self.filepath = filepath
        self.dawayan = self.load_data()

    def load_data(self):
        try:
            with open(self.filepath, 'r') as f:
                data = json.load(f)
            return [Dawai(**item) for item in data]
        except FileNotFoundError:
            return []

    def save_data(self):
        with open(self.filepath, 'w') as f:
            json.dump([d.to_dict() for d in self.dawayan], f, indent=4)

    def add_dwai(self, dawai: Dawai):
        if self.find_dawayan(dawai.name):
            return False
        self.dawayan.append(dawai)
        self.save_data()
        return True

    def find_dawayan(self, name):
        return next((d for d in self.dawayan if d.name.lower() == name.lower()), None)

    def updated_dawayan(self, name, new_price=None, new_availableity=None, new_uses=None):
        daw = self.find_dawayan(name)
        if daw:
            if new_price is not None:
                daw.price = new_price
            if new_availableity is not None:
                daw.available = new_availableity
            if new_uses is not None:
                daw.uses = new_uses
            self.save_data()
            return True
        return False

    def delete_dawayan(self, name):
        daw = self.find_dawayan(name)
        if daw:
            self.dawayan.remove(daw)
            self.save_data()
            return True
        return False

    def all_dawyan(self):
        return [daw for daw in self.dawayan]

    def get_stock_data(self):
        return {d.name: d.price for d in self.dawayan}
