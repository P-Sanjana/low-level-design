# violates Liskov-Substitution principle
class Vehicle:
    def start_engine(self):
        pass

class Car(Vehicle):
    def start_engine(self):
        print('Car engine is starting')

class Bicycle(Vehicle):
    def start_engine(self):
        # doesn't make sense
        pass

# satisfies LSP
class Vehicle:
    def start(self):
        pass

class Car(Vehicle):
    def start(self):
        print("Car engine is starting")

class Bicycle(Vehicle):
    def start(self):
        print("Pedaling the bicycle")
