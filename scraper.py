import requests
from bs4 import BeautifulSoup
import time

class Scraper:
    def __init__(self, base_url):
        self.base_url = base_url

    def scrape_catalogue(self, pages=None, proxy=None):
        scraped_data = []
        page_count = pages if pages else float('inf')
        current_page = 1
        base_headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}

        while current_page <= page_count:
            url = f"{self.base_url}?page={current_page}"
            try:
                response = requests.get(url, proxies={"http": proxy, "https": proxy} if proxy else None, headers=base_headers)
                response.raise_for_status()  # Raise HTTPError for non-200 status codes

                soup = BeautifulSoup(response.text, 'html.parser')
                products = soup.find_all('div', class_='product')

                for product in products:
                    product_title = product.find('h2').text.strip()
                    product_price = float(product.find('span', class_='price').text.strip().replace('$', ''))
                    product_image = product.find('img')['src']

                    scraped_data.append({
                        "product_title": product_title,
                        "product_price": product_price,
                        "path_to_image": product_image
                    })

                current_page += 1
            except requests.RequestException as e:
                print(f"Request error on page {current_page}: {e}")
                time.sleep(5)  # Retry after 5 seconds
            except Exception as e:
                print(f"Error scraping page {current_page}: {e}")
                current_page += 1  # Continue to next page even on error

        return scraped_data
