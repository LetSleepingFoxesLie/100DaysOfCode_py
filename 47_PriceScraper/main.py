from product import Product
from email_account import EmailAccount
import scraper

AMAZON_PRODUCT_ID = "B0874XN4D8"
TEMP_EMAIL = "damawer314@mahmul.com"

# 1. Fetch data
product = scraper.get_ccc_price(product_id = AMAZON_PRODUCT_ID)

# 2. Check against threshold and send email
if product.is_below_threshold(75.00):
    sender = EmailAccount("47_PriceScraper\email.lsfl")
    sender.send_notification(
        to = TEMP_EMAIL,
        product = product
    )