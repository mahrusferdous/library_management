class User:
    def __init__(self, name, library_id, borrowed_book):
        self.__name = name
        self.__library_id = library_id
        self.borrowed_book = []

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_library_id(self):
        return self.__library_id

    def set_library_id(self, library_id):
        self.__library_id = library_id

    def set_borrowed_book(self, borrowed_book):
        self.borrowed_book.append(borrowed_book)

    def display_borrowed_books(self):
        return self.borrowed_book
