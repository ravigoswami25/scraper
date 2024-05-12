from pymongo import MongoClient
from models import Product

class DataStorage:
    def __init__(self, connection_string, database_name, collection_name):
        self.client = MongoClient(connection_string)
        self.db = self.client[database_name]
        self.collection = self.db[collection_name]

    def save_product(self, product: Product):
        product_dict = product.dict()
        existing_product = self.collection.find_one({"product_title": product.product_title})
        if existing_product:
            # Update product if already exists
            self.collection.update_one({"product_title": product.product_title}, {"$set": product_dict})
        else:
            # Insert new product
            self.collection.insert_one(product_dict)

    def is_product_cached(self, product: Product):
        existing_product = self.collection.find_one({"product_title": product.product_title})
        return existing_product is not None
