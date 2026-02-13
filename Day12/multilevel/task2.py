class Animal:
    def __init__(self, category):
        pass
        self.category=category
class Mammal(Animal):
    def __init__(self, category, temperature):
        pass
        self.temperature=temperature
        super().__init__(category)

class Dog(Mammal):
    def __init__(self, category, temperature, breed):
        pass
        self.breed=breed
        super().__init__(category, temperature)
    def describe(self):
        pass
        return f"This is a {self.breed}. It is a {self.temperature} {self.category}."
d1 = Dog("Animal", "Warm-blooded", "Husky")
print( d1.describe())