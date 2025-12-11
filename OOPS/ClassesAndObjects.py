class User:
    def __init__(self, name, age, email):
        self.name = name
        self.age = age
        self.email = email

    def display_info(self):
        print(f"User details - name: {self.name}, age: {self.age}, email: {self.email}")

if __name__ == '__main__':
    user1 = User("Sanjana", 25, "podduturisanjana@gmail.com")
    user1.display_info()
