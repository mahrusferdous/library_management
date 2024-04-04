from book_categories import Book_Categories
from user import User
from author import Author

user_list = []
book_list = []
author_list = []

# all_list = [user_list, book_list, author_list]


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


# Book
def book_operations():
    print(
        "\nBook Operations:\n1. Add a new book\n2. Borrow a boon\n3. Return a book\n4. Search for a book\n5. Display all books"
    )
    choice = handle_choice()
    if choice == 1:
        pass
    elif choice == 2:
        pass
    elif choice == 3:
        pass
    elif choice == 4:
        pass
    elif choice == 5:
        pass
    else:
        print("Invalid choice. Please choose a valid option.")
        return


# User
def user_operations():
    print(
        "\nUser Operations:\n1. Add a new user\n2. View user details\n3. Display all users"
    )
    choice = handle_choice()
    if choice == 1:
        library_id = 0
        name = input("Enter the name of the user: ")
        library_id += 1
        user = User(name, library_id)
        user_list.append(user)
    elif choice == 2:
        pass
    elif choice == 3:
        for user in user_list:
            print(user.get_name())
    else:
        print("Invalid choice. Please choose a valid option.")
        return


# Author
def author_operations():
    print(
        "\nsAuthor Operations:\n1. Add a new author\n2. View author details\n3. Display all authors"
    )
    choice = handle_choice()
    if choice == 1:
        pass
    elif choice == 2:
        pass
    elif choice == 3:
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
