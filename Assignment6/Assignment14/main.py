#14. Aggregation
#Assignment:
#Create a class Department and a class Employee. Use aggregation by having a 
#Department object store a reference to an Employee object that exists independently of it.

class Employee:
    def __init__(self, name):
        self.name = name

    def display(self):
        print(f"Employee Name: {self.name}")

class Department:
    def __init__(self, dept_name, employee):
        self.dept_name = dept_name
        self.employee = employee  # Aggregation: storing reference to an existing Employee object

    def show_details(self):
        print(f"Department: {self.dept_name}")
        self.employee.display()  # Access Employee method

# Create an Employee independently
emp = Employee("Nimra")

# Create a Department and associate it with the Employee
dept = Department("HR", emp)

# Show department details (which uses employee data)
dept.show_details()
