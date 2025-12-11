from abc import ABC, abstractmethod
class Teachable:
    @abstractmethod
    def teach(self):
        pass

class Professor(Teachable):
    def __init__(self, name, subject):
        self.name = name
        self.subject = subject

    def teach(self):
        print(f"{self.name} teaches {self.subject}")

class University:
    def __init__(self, name):
        self.name = name
        self.professors = []

    def add_professor(self, professor):
        self.professors.append(professor)

    def show_professors(self):
        print(f"{self.name} university has following professors:")
        for prof in self.professors:
            prof.teach()

prof1 = Professor("A", "Math")
prof2 = Professor("B", "Science")

university = University("UB")
university.add_professor(prof1)
university.add_professor(prof2)
university.show_professors()

prof1.teach()
prof2.teach()
