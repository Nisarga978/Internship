class User:
    def __init__(self, name, **kwargs):
        pass
        self.name=name
class Driver(User):
    def __init__(self, name, car, **kwargs):
        pass
        self.car=car
        super().__init__(name,**kwargs)

class Rider(User):
    def __init__(self, name, pickup_location, **kwargs):
        pass
        self.pickup_location=pickup_location
        super().__init__(name,**kwargs)

class Trip(Driver, Rider):
    def __init__(self, name, car, pickup_location):
        pass
        super().__init__(name=name,car=car,pickup_location=pickup_location)
    def summary(self):
        pass
        return f"{self.name} will pick up the rider from {self.pickup_location} using {self.car}."
t1 = Trip("Amit", "Honda City", "Sector 21")
print( t1.summary())