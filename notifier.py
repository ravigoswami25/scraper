class Notifier:
    def __init__(self):
        pass

    def notify_scraping_status(self, num_products_scraped: int):
        print(f"Scraping completed. {num_products_scraped} products scraped and updated in DB.")
