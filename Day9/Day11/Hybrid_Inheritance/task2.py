class Person:
    def __init__(self, name, **kwargs):
        pass
        self.name=name
        super().__init__(**kwargs)
class Faculty(Person):
    def __init__(self, name, subject, **kwargs):
        pass
        self.subject=subject
        super().__init__(name,**kwargs)
    def teach(self):
        pass
        
class Staff(Person):
    def __init__(self, name, department, **kwargs):
        pass
        self.department=department
        super().__init__(name,**kwargs)
    def work(self):
        pass

class Administrator(Faculty, Staff):
    def __init__(self, name, subject, department):
        pass
        super().__init__(name=name, subject=subject, department=department)
    def profile_data(self):
        pass
        return f"{self.name} teaches {self.subject} and works in {self.department} department."
a1 = Administrator("Rakesh", "Math", "Operations")
print( a1.profile_data())