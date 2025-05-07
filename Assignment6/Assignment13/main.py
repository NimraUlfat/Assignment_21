#13. Composition
#Assignment:
#Create a class Engine and a class Car. Use composition by passing an Engine
#object to the Car class during initialization. Access a method of the Engine class via the Car class.

class Engine:
    def start(self):
        print("Engine started.")

class Car:
    def __init__(self, engine):
        self.engine = engine  # Composition: Car has an Engine

    def start_car(self):
        print("Starting the car...")
        self.engine.start()  # Accessing Engine's method

# Create an Engine object
engine = Engine()

# Pass the Engine object to Car
car = Car(engine)

# Start the car (which uses the engine)
car.start_car()
