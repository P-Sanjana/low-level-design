from abc import ABC, abstractmethod
class Vehicle(ABC):
    def __init__(self, brand):
        self.brand = brand

    @abstractmethod
    def start(self):
        pass

    def display_brand(self):
        print(f"Brand: {self.brand}")

class Car(Vehicle):
    # def __init__(self, brand):
    #     super().__init__(brand)

    def start(self):
        print("Car is starting")

# car = Car("BMW")
# car.display_brand()
# car.start()

class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass

class Dog(Animal):
    def make_sound(self):
        print("Dog barks")

class Cat(Animal):
    def make_sound(self):
        print("Cat meows")

dog = Dog()
dog.make_sound()

cat = Cat()
cat.make_sound()
