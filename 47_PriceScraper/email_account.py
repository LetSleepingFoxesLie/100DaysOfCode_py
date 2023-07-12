from smtplib import SMTP
from product import Product

class EmailAccount:
    def __init__(self, file_path: str):
        try:
            with open (file_path, "r") as f:
                self.username = f.readline().strip("\n\t")
                self.password = f.readline().strip("\n\t")
        except FileNotFoundError:
            print("File not found.")
            self.username = ":)"
            self.password = ":("

    def send_notification(self, to: str, product: Product) -> None:
        
        message = self.compose_email(product)
        
        with SMTP("smtp.gmail.com", port = 587) as connection:
            connection.starttls()
            
            connection.login(
                user = self.username,
                password = self.password
            )
            
            connection.sendmail(
                from_addr = self.username,
                to_addrs = to,
                msg = message.encode("utf-8")
            )
            

    def compose_email(self, product: Product) -> str:
        AMAZON_BASE = "https://amazon.com/dp/"
        
        title = "Subject:[AmazonDeals] Product with great prices!\n\n"
        
        body = f"Hello!\n\nLook at what this great deal we found for [{product.name}]!\n"
        body += f"Buy it for ${product.price} on Amazon right now: {AMAZON_BASE + product.amazon_id}"
        
        message = title + body
        return message