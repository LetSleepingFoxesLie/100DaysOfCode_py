class Product:
    def __init__(self, name: str, amazon_id: str, price: float):
        self.name = name
        self.amazon_id = amazon_id
        self.price = price
        
        
    def is_below_threshold(self, threshold: float) -> bool:
        return self.price <= threshold