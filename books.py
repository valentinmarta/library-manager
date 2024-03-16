class Book:

    def __init__(self, id, name, author, state):
        self.id = id
        self.name = name
        self.author = author
        self.state = state

    def present(self):
        print(f"Id: {self.id}, Name: {self.name}, Author: {self.author}, State: {self.state}")

    def type(self):
        print(f"Book type: {type(self).__name__}")

    def rented(self):
        self.state = "rented"

    def returned(self):
        self.state = "returned"

class BookKids(Book):

    def __init__(self, id, name, author, state, minimum_age):
        super().__init__(id, name, author, state)
        self.minimum_age = minimum_age

class LanguageBook(Book):

    def __init__(self, id, name, author, state, language):
        super().__init__(id, name, author, state)
        self.language = language