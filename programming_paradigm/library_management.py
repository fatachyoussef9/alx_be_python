class Book :
    def __init__(self, title, author ) :
        self.title = title 
        self.author = author
        self._is_checked_out = False 

    def check_out(self):
        if not self._is_checked_out:
            self._is_checked_out = True
            return True
        return False
    
    def return_book(self):
        if self._is_checked_out:
            self._is_checked_out = False
            return True
        return False
    
    def is_available(self):
        """Returns whether the book is available to be checked out."""
        return not self._is_checked_out

class Library :
    def __init__(self):
        self._books = []  # Private list to store the books

    def add_book(self, book: Book):
        self._books.append(book)

    def check_out_book(self, title):
        """Checks out a book by its title, if available."""
        book: Book
        for book in self._books:
            if book.title == title:
                if book.check_out():
                    print(f"'{title}' has been checked out.")
                else:
                    print(f"'{title}' is already checked out.")
                return
        print(f"'{title}' is not in the library.")

    def return_book(self, title):
        """Returns a book by its title, if it's checked out."""
        book: Book
        for book in self._books:
            if book.title == title:
                if book.return_book():
                    print(f"'{title}' has been returned.")
                else:
                    print(f"'{title}' was not checked out.")
                return
        print(f"'{title}' is not in the library.")

    def list_available_books(self):
        """Lists all available books in the library."""
        book: Book
        available_books = [book for book in self._books if book.is_available()]
        if available_books:
            for book in available_books:
                print(f"{book.title} by {book.author}")
        else:
            print("No available books.")

