# Base class
class Vehicle:
    def move(self):
        print("This vehicle moves in some way.")

# Subclasses with different move() behavior
class Car(Vehicle):
    def move(self):
        print("Driving 🚗")

class Plane(Vehicle):
    def move(self):
        print("Flying ✈️")

class Bicycle(Vehicle):
    def move(self):
        print("Pedaling 🚴")

