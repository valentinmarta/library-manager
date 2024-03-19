from books import *

class Manager:

    def __init__(self):
        self.book_list : list[Book] = []
        self.language = {
        "en":"english", 
        "ge":"german",
        "ch":"chinese"
        }

    def book_type(self):
        
        while True:
            list = []

            for book in Book.__subclasses__():
                print(book.__name__)
                list.append(book.__name__)

            print(Book.__name__)
            list.append(Book.__name__)

            op = input("Choose one type of book: ")

            if op in list:
                return op
            else:
                print("That type of book doesn't exist. Please try again.")

    def check_id(self):
        
        while True:

            flag = True

            try:
                id = int(input("Choose the id: "))
            except Exception as e:
                print(f"Error: {e}")
                flag = False

            for book in self.book_list:
                if id == book.id:
                    print("This id already exist. Try again.")
                    flag = False

            if flag:
                return id
                

    def save_book(self, id, name, author):
        
        try:
            file = open("books.txt", "a+")
            file.write(f"Id: {id}, Name: {name}, Author: {author}\n")
            file.close()
        except Exception as e:
            print(e)

    def choose_language(self):
        print("Below is a list of available languages: ")

        for i in self.language:
            print(f"key: {i}, language: {self.language[i]}")

        op = input("Choose a language by entering its key. If you enter something else, the default language will be english.")

        language = self.language.get(op, "english")
        return language


    #First option
    def create_book(self):
        pass

    #Second option
    def show_books(self):
        pass

    #Third option
    def change_state(self):
        pass