import json
from datetime import datetime, timedelta
import os

class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.id = isbn
        self.is_available = True
        self.due_date = None

    def to_dict(self):
        return {
            'title': self.title,
            'author': self.author,
            'id': self.id,
            'is_available': self.is_available,
            'due_date': self.due_date.strftime('%Y-%m-%d') if self.due_date else None
        }
    
    @staticmethod
    def from_dict(data):
        book = Book(data['title'], data['author'], data['id'])
        book.is_available = data['is_available']
        if data['due_date']:
            book.due_date = datetime.strptime(data['due_date'], '%Y-%m-%d')
        return book

    def __str__(self):
        return f"Book(title='{self.title}', author='{self.author}', id='{self.id}', is_available={self.is_available})"

class Member:
    def __init__(self, name, id):
        self.name = name
        self.id = id
        self.borrowed_books = []

    def borrow_book(self, book):
        if book.is_available:
            
            # Mark the book as borrowed
            book.is_available = False

            # Set due date to 1 week from today
            date_today = datetime.now()
            book.due_date = date_today + timedelta(days=7)  # 1 weeks loan period

            # Save the due_date into the book in string format (so it can be stored in JSON).
            book.due_date = book.due_date.strftime("%Y-%m-%d")

            # Add book to member's borrowed books
            self.borrowed_books.append(book)

            print(f"{self.name} has successfully borrowed {book.title}. Due date is {book.due_date}.")
        else:
            print(f"Sorry, {book.title} is currently not available.")

    def return_book(self, book):
        if book in self.borrowed_books:
            book.is_available = True

            if book.due_date:
                due_date = datetime.strptime(book.due_date, "%Y-%m-%d")
                date_today = datetime.now()
                if date_today > due_date:
                    late_days = (date_today - due_date).days
                    fine = late_days * 1  # Assuming $1 fine per late day
                    print(f"{self.name} has returned {book.title} late by {late_days} days. Fine incurred: ${fine}.")
                else:
                    print(f"{self.name} has returned {book.title} on time. No fine incurred.")

            self.borrowed_books.remove(book)
        else:
            print(f"{self.name} did not borrow {book.title}.")

class Library:
    def __init__(self):
        self.books = []
        self.members = []
        self.data_folder = 'data'
        self.books_file = 'books.json'
        self.db_path = os.path.join(self.data_folder, self.books_file)
        self.load_books()

    def load_books(self,):
        if os.path.exists(self.data_folder):
            try:
                with open(self.db_path, 'r') as f:
                    books_data = json.load(f)
                    self.books = [Book.from_dict(book) for book in books_data]
            except FileNotFoundError:
                self.books = []
        else:
            self.books = []

    def save_books(self):
        if not os.path.exists(self.data_folder):
            os.makedirs(self.data_folder)

        data = [book.to_dict() for book in self.books]

        with open(self.db_path, 'w') as f:
            json.dump(data, f, indent=4)

    def add_book(self, book):
        self.books.append(book)
        self.save_books()

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

        