from abc import ABC, abstractmethod

class Movable(ABC):
    @abstractmethod
    def move(self):
        pass

class Car(Movable):
    pass
    def move(self):
        return f"Car is driving"
class Bike(Movable):
    pass
    def move(self):
        return f"Bike is riding"
c = Car()
print( c.move())