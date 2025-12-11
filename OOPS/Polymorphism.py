class Math:
    def add(self, a, b, c=0):
        return a + b + c

class Animal:
    def make_sound(self):
        print("Animal sound")

class Dog(Animal):
    def make_sound(self):
        print("Dog barks")

class Cat(Animal):
    def make_sound(self):
        print("Cat meows")

animals = [Dog(), Cat()]
for animal in animals:
    animal.make_sound()

# m = Math()
# print(m.add(2, 3))
# print(m.add(2, 3, 4))