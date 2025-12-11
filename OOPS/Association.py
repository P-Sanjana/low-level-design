class Library:
    def __init__(self, name):
        self.name = name
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def show_books(self):
        print(f"Books in {self.name}:")
        for book in self.books:
            print(book.name)

class Book:
    def __init__(self, name, library):
        self.name = name
        self.library = library

    def show_library(self):
        print(f"{self.name} is in {self.library.name}")

lib = Library("City Library")
book1 = Book("1982", lib)
book2 = Book("New City", lib)
lib.add_book(book1)
lib.add_book(book2)
lib.show_books()

book1.show_library()
book2.show_library()