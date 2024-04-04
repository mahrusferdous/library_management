from book_categories import Book_Categories
from user import User
from author import Author


class Main:
    def __init__(self):
        print("Welcome to the Library Management System!")
        self.main_menu()

    def main_menu(self):
        while True:
            print(
                "Main Menu\n1. Book Operations\n2. User Operations\n3. Author Operations\n4. Quit"
            )
            if self.handle_choice() == 1:
                self.book_operations()
            elif self.handle_choice() == 2:
                self.user_operations()
            elif self.handle_choice() == 3:
                self.author_operations()
            elif self.handle_choice() == 4:
                print("Thank you for using the Library Management System!")
                break
            else:
                print("invalid choice. Please choose a valid option.")

    def handle_choice(self):
        try:
            choice = int(input("Choose an option: "))
            return choice
        except ValueError:
            print("Invalid choice. Please choose a valid option.")
            return
        except Exception as e:
            print(e)
            return

    def book_operations(self):
        print(
            "Book Operations:\n1. Add a new book\n2. Borrow a boon\n3. Return a book\n4. Search for a book\n5. Display all books"
        )
        if self.handle_choice() == 1:
            pass
        elif self.handle_choice() == 2:
            pass
        elif self.handle_choice() == 3:
            pass
        elif self.handle_choice() == 4:
            pass
        elif self.handle_choice() == 5:
            pass
        else:
            print("Invalid choice. Please choose a valid option.")
            return

        def user_operations(self):
            print(
                "User Operations:\n1. Add a new user\n2. View user details\n3.Display all users"
            )
            if self.handle_choice() == 1:
                pass
            elif self.handle_choice() == 2:
                pass
            elif self.handle_choice() == 3:
                pass
            else:
                print("Invalid choice. Please choose a valid option.")
                return

        def author_operations(self):
            print(
                "Author Operations:\n1. Add a new author\n2. View author details\n3. Display all authors"
            )
            if self.handle_choice() == 1:
                pass
            elif self.handle_choice() == 2:
                pass
            elif self.handle_choice() == 3:
                pass
            else:
                print("Invalid choice. Please choose a valid option.")
                return


main = Main()
