#6. Constructors and Destructors
#Assignment:
#Create a class Logger that prints a message when an object is created 
#(constructor) and another message when it is destroyed (destructor).

class Logger:
    def __init__(self):
        print("Logger object created.")

    def __del__(self):
        print("Logger object destroyed.")

# Creating an object
log = Logger()

# Deleting the object manually 
del log

# If not deleted manually, it will be destroyed when the program ends
