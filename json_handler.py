import json
from dawai import Dawai

FILE_PATH = "medicines.json"

import json

def save_medicines_to_json(medicines):
    try:
        with open(FILE_PATH, "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        data = []

    # Clear existing data if we're saving a complete list
    if isinstance(medicines, list):
        data = []  # Clear existing data
        for medicine in medicines:
            data.append(medicine.to_dict())
    else:
        # Single medicine object
        data.append(medicines.to_dict())

    with open(FILE_PATH, "w") as file:
        json.dump(data, file, indent=4)
def load_medicines_from_json():
    try:
        with open('medicines.json', 'r') as f:
            data = json.load(f)
            # Convert the data back into Dawai objects
            medicines = []
            for item in data:
                medicines.append(Dawai(item['name'], item['uses'], item['price'], item['available'], item['stock']))
            return medicines
    except FileNotFoundError:
        return []  # Return an empty list if no file exists
