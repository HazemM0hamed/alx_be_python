class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self._is_checked_out = False
    
    def get_title(self):
        return self.title
    
    def get_author(self):
        return self.author
    
    def is_checked_out(self):
        return self._is_checked_out
    
    def check_out(self):
        self._is_checked_out = True
    
    def return_book(self):
        self._is_checked_out = False
class Library:
    def __init__(self):
        self._books = []
    
    def add_book(self, book):
        self._books.append(book)
    
    def check_out_book(self, title):
        for book in self._books:
            if book.get_title() == title and not book.is_checked_out():
                book.check_out()
                print(f"Checked out '{title}' successfully.")
                return
        print(f"Book '{title}' is either not available or already checked out.")
    
    def return_book(self, title):
        for book in self._books:
            if book.get_title() == title and book.is_checked_out():
                book.return_book()
                print(f"Returned '{title}' successfully.")
                return
        print(f"Book '{title}' is either not available or already returned.")
    
    def list_available_books(self):
        available_books = [book.get_title() for book in self._books if not book.is_checked_out()]
        if available_books:
            print("Available books:")
            for book_title in available_books:
                print(f"   {book_title}")
        else:
            print("No books available.")


