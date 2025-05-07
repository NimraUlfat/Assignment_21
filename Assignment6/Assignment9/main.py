#9. Abstract Classes and Methods
#Assignment:
#Use the abc module to create an abstract class Shape with an abstract method area(). 
#Inherit a class Rectangle that implements area().

from abc import ABC, abstractmethod

# Abstract class
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass  # Abstract method has no implementation

# Subclass implementing the abstract method
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

# Create an object of Rectangle
rect = Rectangle(5, 10)
print("Area of rectangle:", rect.area())
