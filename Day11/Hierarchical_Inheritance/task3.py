class Person:
    def __init__(self, name, emp_id):
        pass
        self.name=name
        self.emp_id=emp_id
class Manager(Person):
    def __init__(self, name, emp_id, department):
        pass
        self.department=department
        super().__init__(name,emp_id)
    def get_profile_data(self):
        pass
        return f"{self.name} (ID: {self.emp_id}) is a manager of {self.department} department."
class Engineer(Person):
    def __init__(self, name, emp_id, specialization):
        pass
        self.specialization=specialization
        
        super().__init__(name,emp_id)
    def get_profile_data(self):
        pass
        return f"{self.name} (ID: {self.emp_id}) is a {self.specialization.lower()} engineer."
m1 = Manager("Kavita", 101, "HR")
print( m1.get_profile_data())