#3. Public Variables and Methods
#Assignment:
#Create a class Car with a public variable brand and a public method start(). 
# Instantiate the class and access both from outside the class.

class Car:
    # Constructor with public variable
    def __init__(self, brand):
        self.brand = brand  # Public variable

    # Public method
    def start(self):
        print(f"{self.brand} car has started.")

# Object creation
car1 = Car("Rolls-Royce")

# Accessing public variable
print("Brand:", car1.brand)

# Calling public method
car1.start()
