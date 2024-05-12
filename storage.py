from models import Product
import json

class DataStorage:
    def __init__(self, filename):
        self.filename = filename

    def load_from_json(self):
        try:
            with open(self.filename, 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            return []

    def save_to_json(self, data):
        with open(self.filename, 'w') as file:
            json.dump(data, file)

    def update_storage(self, new_data):
        current_data = self.load_from_json()
        current_data.extend(new_data)
        self.save_to_json(current_data)

    def is_product_cached(self, product: Product):
        current_data = self.load_from_json()
        for item in current_data:
            if item["product_title"] == product.product_title:
                return True
        return False
