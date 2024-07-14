class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self._is_checked_out = False

    def check_out(self):
        if not self._is_checked_out:
            self._is_checked_out = True
            return f"{self.title} by {self.author} has been checked out."
        else:
            return f"{self.title} by {self.author} is already checked out."

    def return_book(self):
        if self._is_checked_out:
            self._is_checked_out = False
            return f"{self.title} by {self.author} has been returned."
        else:
            return f"{self.title} by {self.author} was not checked out."

    def is_checked_out(self):
        return self._is_checked_out


class Library:
    def __init__(self):
        self._books = []

    def add_book(self, book):
        self._books.append(book)
        return f"{book.title} by {book.author} has been added to the library."

    def check_out_book(self, title):
        for book in self._books:
            if book.title == title:
                return book.check_out()
        return f"No book with the title '{title}' was found in the library."

    def return_book(self, title):
        for book in self._books:
            if book.title == title:
                return book.return_book()
        return f"No book with the title '{title}' was found in the library."

    def list_available_books(self):
        available_books = [book for book in self._books if not book.is_checked_out()]
        if available_books:
            return "\n".join([f"{book.title} by {book.author}" for book in available_books])
        else:
            return "No available books in the library."