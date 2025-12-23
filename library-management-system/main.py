from src.func import Book, Member, Library
import os

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

Library_System = Library()

while True:

    print("===============================================")
    print("    Library Management System - Main Module")
    print("===============================================")

    print("1. [ADMIN] Add Books to Library")
    print("2. [ADMIN] Register New Members")
    print("3. [TRANSACTION] Lend Books")
    print("4. [TRANSACTION] Return Books")
    print("5. [INFO] View Library Status")
    print("6. [INFO] View Member Status")
    print("7. Exit")
    print('===============================================')

    # Input user
    choice = input("Select an option (1-6): ")

    # Process user choice
    if choice == '1':
        
        print('--- ADD BOOKS TO LIBRARY ---')

        title = input("Enter book title: ")
        author = input("Enter book author: ")
        isbn = input("Enter book ISBN: ")
        book = Book(title, author, isbn)
        Library_System.add_book(book)

        print(f"Book '{title}' added to library.")
        input("Press Enter to continue...")
        clear_console()

    elif choice == '2':
        
        print('--- REGISTER NEW MEMBER ---')

        name = input("Enter member name: ")
        member_id = input("Enter member ID: ")
        member = Member(name, member_id)
        Library_System.register_member(member)

        print(f"Member '{name}' registered.")
        input("Press Enter to continue...")
        clear_console()

    elif choice == '3':
        
        print('--- LEND BOOK ---')

        book_id = input("Enter book ID to lend: ")
        member_id = input("Enter member ID: ")

        Library_System.lend_book(book_id, member_id)

        print('Validating transaction...')
        print(f'- Member : {member_id} requested book ID {book_id}.')
        if any(b.id == book_id and b.is_available for b in Library_System.books):
            print(f'- Book   : {book_id} is available and has been lent out.')
        else:
            print(f'- Book   : {book_id} is currently not available.')

        print("Transaction complete.")
        input("Press Enter to continue...")
        clear_console()

    elif choice == '4':
        
        print('--- RETURN BOOK ---')

        book_id = input("Enter book ID to return: ")
        member_id = input("Enter member ID: ")
        Library_System.receive_book(book_id, member_id)

        print("Return process complete.")
        input("Press Enter to continue...")
        clear_console()

    elif choice == '5':
        
        print('--- LIBRARY STATUS ---')

        print('ID      | Title                 | Author               | Available')
        print('---------------------------------------------------------------') 

        for book in Library_System.books:
            print(f"{book.id:7} | {book.title:20} | {book.author:18} | {'Yes' if book.is_available else 'No'}")

        print('---------------------------------------------------------------')
        print(f'Total Books: {len(Library_System.books)}')
        input("Press Enter to continue...")
        clear_console()

    elif choice == '6':
        
        print('--- MEMBER STATUS ---')

        for member in Library_System.members:
            print(f"Member ID: {member.id}, Name: {member.name}")
            if member.borrowed_books:
                print("  Borrowed Books:")
                for book in member.borrowed_books:
                    print(f"    - {book.title} by {book.author} (ID: {book.id})")
            else:
                print("  No borrowed books.")
            print('---------------------------------------------------------------')

        input("Press Enter to continue...")
        clear_console()

    elif choice == '7':
        print("Exiting the Library Management System. Goodbye!")
        break

    else:
        print("Invalid option. Please select a number between 1 and 6.")
        input("Press Enter to continue...")
        clear_console()