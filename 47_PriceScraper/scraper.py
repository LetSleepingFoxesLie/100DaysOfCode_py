import requests
from bs4 import BeautifulSoup

from product import Product

def get_ccc_price(product_id: str) -> Product:
    url = f"https://camelcamelcamel.com/product/{product_id}?active=price_amazon&context=home_popular"
    
    response = requests.get(url,
                            headers = {
                                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
                            })
    soup = BeautifulSoup(response.text, "html.parser")
    
    #print(soup)
    
    product_name_tag = soup.select_one("div div h2 a")
    # print(product_name_tag)
    
    product_price_tag = soup.select_one("p span span")
    # print(product_price_tag)
    product_price = float(product_price_tag.text.strip("$"))
    # print(product_price)
    
    return Product(
        name = product_name_tag.text,
        amazon_id = product_id,
        price = product_price
    )