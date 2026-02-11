class Mobile:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price

    def __eq__(self, other):
        if not isinstance(other, Mobile):
            return False
        return self.brand == other.brand and self.model == other.model

mobile1 = Mobile("Apple", "iPhone 15", 80000)
mobile2 = Mobile("Apple", "iPhone 15", 90000)
mobile3 = Mobile("Samsung", "S24", 75000)

print(mobile1 == mobile2)  
print(mobile1 == mobile3)  
print(mobile2 == mobile3) 
