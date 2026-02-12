class Product:
    def __init__(self, name, **kwargs):
        pass
        self.name=name
class DigitalProduct(Product):
    def __init__(self, name, size, **kwargs):
        pass
        self.size=size
        super().__init__(name,**kwargs)
class PhysicalProduct(Product):
    def __init__(self, name, weight, **kwargs):
        pass
        self.weight=weight
        super().__init__(name,**kwargs)
class HybridProduct(DigitalProduct, PhysicalProduct):
    def __init__(self, name, size, weight):
        pass
        super().__init__(name=name,size=size,weight=weight)
    def details(self):
        pass
        return f"{self.name} includes {self.size} digital files and weighs {self.weight}."
hp1 = HybridProduct("Python Mastery", "2GB", "1kg")
print( hp1.details())