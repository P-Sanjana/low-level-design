class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(f"{self.name} is eating.")

    def make_sound(self):
        print("Animal sound.")

class Dog(Animal):
    def __init__(self, name, color):
        super().__init__(name)
        self.color = color

    def bark(self):
        print(f"{self.name} is barking.")

    def make_sound(self):
        print("Dog sound.")


if __name__ == "__main__":
    dog = Dog("Buddy", "white")
    dog.eat()
    dog.bark()
    dog.make_sound()
