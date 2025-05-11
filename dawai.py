# dawai.py

class Dawai:
    def __init__(self, name, uses, price, available=True, stock=1):
        self.name = name.strip().lower() 
        self.uses = uses
        self.price = price
        self.available = available
        self.stock = stock

    def display_info(self):
        status = "✅ Available" if self.available else "❌ Not Available"
        return f"""
    **Name:** {self.name.title()}  
    **Uses:** {self.uses}  
    **Price:** PKR= {self.price}  
    **Stock:** {self.stock} units  
    **Status:** {status}
    """


    def to_dict(self):
        return {
            "name": self.name,
            "uses": self.uses,
            "price": self.price,
            "available": self.available,
            "stock": self.stock
        }

