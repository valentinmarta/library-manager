from manager import *

def main():

    object = Manager()

    while True:
    
        op = input("""------> Library managment <------
        1.   Create books.
        2.   Show books that are available.
        3.   Change the availability of the books (rented or returned).
        4.   Exit.
        Option: """)

        if op == "1":
            object.create_book()
        elif op == "2":
            object.show_books()
        elif op == "3":
            pass
        elif op == "4":
            break
        else:
            print("Invalid value. Please try again.")


if __name__ == "__main__":
    main()