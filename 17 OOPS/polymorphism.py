class Vehicle:
    def __init__(self):
        self.brand = ""
        self.model = ""
    def move(self):
        print("Move!")

class Car(Vehicle):
    def move(self):
        print("Drive!")
class Boat(Vehicle):
    def move(self):
        print("Sail!")

class Plane(Vehicle):
    def move(self):
        print("Fly!")

car1 = Car()
boat1 = Boat()
plane1 = Plane()

for x in (car1,boat1,plane1):
    x.move()