class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self._is_checked_out = False


    def check_out(self):
        if not self._is_checked_out:
            self._is_checked_out = True
            return f'the book {self.title} by {self.author} is now checked out'
        else:
            return f"The book '{self.title}' by {self.author} is already checked out."

    def return_book(self):
        if self._is_checked_out:
            self._is_checked_out =False
            return f'the book {self.title} by {self.author} has been returned'
        else:
            return f"The book '{self.title}' by {self.author} was not checked out."



class Library():
    def __init__(self):
        self._books = []

    def add_book(self,book):
        for exist_book in self._books:
            if exist_book.title == book.title:
                print(f'Book {book.title} already exists in the library')
                break
        else:
            self._books.append(book)

    def check_out_book(self,title):
        for book in self._books:
            if book.title == title:
                return book.check_out()
        return f'no book with title {title} found'

    def return_book(self, title):
        for book in self._books:
            if book.title == title:
                return book.return_book()
        return f'no book with title {title} found'


    def list_available_books(self):
        for book in self._books:
            if not book._is_checked_out:
                print(f'{book.title} by {book.author}')

