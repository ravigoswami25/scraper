from fastapi import FastAPI, HTTPException, Depends
from models import Settings, Product
from scraper import Scraper
from storage import DataStorage
from notifier import Notifier
from in_memory_db import InMemoryDB

app = FastAPI()

# Redis connection details
REDIS_HOST = "localhost"
REDIS_PORT = 6379
REDIS_DB = 0

storage = DataStorage("mongodb://username:password@localhost:27017", "scraped_data_db", "products")
notifier = Notifier()
db = InMemoryDB(REDIS_HOST, REDIS_PORT, REDIS_DB)

# Simple authentication using a static token
API_KEY = "your_static_token"

# Dependency to validate API key
def authenticate(api_key: str):
    if api_key != API_KEY:
        raise HTTPException(status_code=401, detail="Invalid API Key")

# API endpoint to trigger scraping
@app.post("/scrape")
def scrape_website(settings: Settings, api_key: str = Depends(authenticate)):
    scraper = Scraper("https://dentalstall.com/shop/")
    scraped_data = scraper.scrape_catalogue(pages=settings.pages, proxy=settings.proxy)

    num_products_updated = 0
    for product_dict in scraped_data:
        product = Product(**product_dict)
        if not storage.is_product_cached(product) or db.is_price_changed(product):
            storage.save_product(product)
            db.update_cache(product)
            num_products_updated += 1

    notifier.notify_scraping_status(num_products_updated)
    return {"message": f"Scraping completed. Updated {num_products_updated} products in DB."}
