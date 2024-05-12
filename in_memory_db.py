from models import Product

class InMemoryDB:
    def __init__(self):
        self.cache = {}

    def is_price_changed(self, product: Product):
        if product.product_title in self.cache:
            return self.cache[product.product_title] != product.product_price
        return True

    def update_cache(self, product: Product):
        self.cache[product.product_title] = product.product_price
