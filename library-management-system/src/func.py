class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.id = isbn
        self.is_available = True

    def __str__(self):
        return f"Book(title='{self.title}', author='{self.author}', id='{self.id}', is_available={self.is_available})"

class Member:
    def __init__(self, name, id):
        self.name = name
        self.id = id
        self.borrowed_books = []

    def borrow_book(self, book):
        if book.is_available:
            book.is_available = False
            self.borrowed_books.append(book)
        else:
            print(f"Sorry, {book.title} is currently not available.")

    def return_book(self, book):
        if book in self.borrowed_books:
            book.is_available = True
            self.borrowed_books.remove(book)
        else:
            print(f"{self.name} did not borrow {book.title}.")

class Library:
    def __init__(self):
        self.books = []
        self.members = []

    def add_book(self, book):
        self.books.append(book)

    def register_member(self, member):
        self.members.append(member)

    def lend_book(self, book_id, member_id):
        book = next((b for b in self.books if b.id == book_id), None)
        member = next((m for m in self.members if m.id == member_id), None)

        if book and member:
            member.borrow_book(book)
        else:
            return 0;

    def receive_book(self, book_id, member_id):
        book = next((b for b in self.books if b.id == book_id), None)
        member = next((m for m in self.members if m.id == member_id), None)

        if book and member:
            member.return_book(book)
        else:
            return 0;

        