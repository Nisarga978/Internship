class Organization:
    def __init__(self, company):
        pass
        self.company=company
class Department(Organization):
    def __init__(self, company, dept):
        pass
        self.dept=dept
        super().__init__(company)
class Employee(Department):
    def __init__(self, company, dept, emp_name):
        pass
        self.emp_name=emp_name
        super().__init__(company,dept)

    def get_details(self):
        pass
        return f"{self.emp_name} works in {self.dept} department at {self.company}"
e1 = Employee("Innotech", "HR", "Meera")
print(e1.get_details())