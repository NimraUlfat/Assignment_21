#7. Access Modifiers: Public, Private, and Protected
#Assignment:
#Create a class Employee with:
#a public variable name,
#a protected variable _salary, and
#a private variable __ssn.
#Try accessing all three variables from an object of the class and document what happens.

class Employee:
    def __init__(self, name, salary, ssn):
        self.name = name        # Public 
        self._salary = salary   # Protected 
        self.__ssn = ssn        # Private

# Create an object
emp = Employee("Nimra", 10000, "123-56")

# Access public variable
print("Public (name):", emp.name)

# Access protected variable
print("Protected (_salary):", emp._salary)

# Access private variable
try:
    print("Private (__ssn):", emp.__ssn)
except AttributeError as e:
    print("Private (__ssn): Cannot access directly -", e)

# Accessing private variable using name mangling
print("Private accessed via name mangling:", emp._Employee__ssn)
