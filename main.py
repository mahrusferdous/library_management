from book_categories import Book_Categories
from user import User
from author import Author


def handle_choice():
    try:
        choice = int(input("Choose an option: "))
        return choice
    except ValueError:
        print("Invalid choice. Please choose a valid option.")
        return
    except Exception as e:
        print(e)
        return


def book_operations():
    print(
        "\nBook Operations:\n1. Add a new book\n2. Borrow a boon\n3. Return a book\n4. Search for a book\n5. Display all books"
    )
    if handle_choice() == 1:
        pass
    elif handle_choice() == 2:
        pass
    elif handle_choice() == 3:
        pass
    elif handle_choice() == 4:
        pass
    elif handle_choice() == 5:
        pass
    else:
        print("Invalid choice. Please choose a valid option.")
        return


def user_operations():
    print(
        "\nUser Operations:\n1. Add a new user\n2. View user details\n3.Display all users"
    )
    if handle_choice() == 1:
        pass
    elif handle_choice() == 2:
        pass
    elif handle_choice() == 3:
        pass
    else:
        print("Invalid choice. Please choose a valid option.")
        return


def author_operations():
    print(
        "\nsAuthor Operations:\n1. Add a new author\n2. View author details\n3. Display all authors"
    )
    if handle_choice() == 1:
        pass
    elif handle_choice() == 2:
        pass
    elif handle_choice() == 3:
        pass
    else:
        print("Invalid choice. Please choose a valid option.")
        return


print("\nWelcome to the Library Management System!")
while True:
    print(
        "\nMain Menu\n1. Book Operations\n2. User Operations\n3. Author Operations\n4. Quit"
    )
    choice = handle_choice()
    if choice == 1:
        book_operations()
    elif choice == 2:
        user_operations()
    elif choice == 3:
        author_operations()
    elif choice == 4:
        print("Thank you for using the Library Management System!")
        break
    else:
        print("invalid choice. Please choose a valid option.")
