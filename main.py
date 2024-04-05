from book_categories import Book_Categories
from user import User
from author import Author

book1 = Book_Categories(
    "The Alchemist",
    "Paulo Coelho",
    "9780062315007",
    "Action and Adventure",
    "April 25, 2006",
    "Available",
    "Fiction",
)
book2 = Book_Categories(
    "The Great Gatsby",
    "F. Scott Fitzgerald",
    "9780743273565",
    "Action and Adventure",
    "September 30, 2004",
    "Available",
    "Fiction",
)
user1 = User("Tom Cat", 1)
user2 = User("Jerry Mouse", 2)
author1 = Author(
    "The Alchemist",
    "Paulo Coelho",
    "Paulo Coelho was born in Rio de Janeiro, Brazil, in 1947.",
)
author2 = Author(
    "The Great Gatsby",
    "F. Scott Fitzgerald",
    "F. Scott Fitzgerald was born in St. Paul, Minnesota, in 1896.",
)

book_list = [book1, book2]
user_list = [user1, user2]
author_list = [author1, author2]


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
        "\nBook Operations:\n1. Add a new book\n2. Borrow a book\n3. Return a book\n4. Search for a book\n5. Display all books"
    )
    choice = handle_choice()
    if choice == 1:
        title = input("Enter the title of the book: ")
        author = input("Enter the author of the book: ")
        ISBN = input("Enter the ISBN of the book: ")
        genre = input("Enter the genre of the book: ")
        publication_date = input("Enter the publication date of the book: ")
        availability = input("Enter the availability of the book: ")
        book = Book_Categories(
            title, author, ISBN, genre, publication_date, availability
        )
        book.choose_category()
        book_list.append(book)
    elif choice == 2:
        pass
    elif choice == 3:
        pass
    elif choice == 4:
        book = input("Enter the title of the book you want to search for: ")
        for i in range(len(book_list)):
            if book in book_list[i].get_title():
                print(
                    f"Book title: {book_list[i].get_title()}\nAuthor: {book_list[i].get_author()}\nISBN: {book_list[i].get_ISBN()}\nGenre: {book_list[i].get_genre()}\nPublication Date: {book_list[i].get_publication_date()}\nAvailability: {book_list[i].get_availability()}\nCategory: {book_list[i].get_categories()}"
                )
            else:
                print("Book not found.")
    elif choice == 5:
        for i in range(len(book_list)):
            print(f"{i+1}. {book_list[i].get_title()}")
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
        for user in user_list:
            print(user.display_borrowed_books())
    elif choice == 3:
        for i in range(len(user_list)):
            print(f"{i+1}. {user_list[i].get_name()}")
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
        name = input("Enter the name of the user: ")
        biography = input("Write a little bit about the author: ")
        author = Author(name, biography)
        author_list.append(author)
    elif choice == 2:
        for author in author_list:
            print(
                f"Author's name is {author.get_name()} and Biography: {author.get_biography()}"
            )
    elif choice == 3:
        for i in range(len(author_list)):
            print(f"{i+1}. {author_list[i].get_name()}")
    else:
        print("Invalid choice. Please choose a valid option.")
        return


# Main functionality
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
