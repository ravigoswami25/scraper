import redis
from models import Product

class InMemoryDB:
    def __init__(self, redis_host, redis_port, redis_db):
        self.redis_client = redis.Redis(host=redis_host, port=redis_port, db=redis_db)

    def is_price_changed(self, product: Product):
        cached_price = self.redis_client.get(product.product_title)
        if cached_price:
            return float(cached_price) != product.product_price
        return True

    def update_cache(self, product: Product):
        self.redis_client.set(product.product_title, product.product_price)
