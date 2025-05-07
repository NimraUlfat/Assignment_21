#2. Using cls
#Assignment:
#Create a class Counter that keeps track of how many objects have been created. 
#Use a class variable and a class method with cls to manage and display the count.

class Counter:
    count = 0  

    def __init__(self):
        Counter.count += 1  # Increment count when object is created

    @classmethod
    def display_count(cls):
        print(f"Total objects created: {cls.count}")

# Creating objects
obj1 = Counter()
obj2 = Counter()
obj3 = Counter()

# Display total count using class method
Counter.display_count()
