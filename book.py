"""
Overview: Enhance the existing Library Management CLI Project by implementing a 
Lend Book feature that allows users to borrow books and updates the system accordingly.
Requirements: 
- Add a "Lend Book" option to the existing Library Management CLI menu.
- When someone borrows book, collect borrower's name, phone number, 
    book title, and assign a return due date using datetime. Save them in a file.
- When someone lends a book, the quantity of the book will decrease.
- When the borrower returns the book, remove their lend info from the lend book file.
- When the borrower returns the book, the quantity of the book will increase.
- If there are no books available to lend, a message should be printed saying, 
    "There are not enough books available to lend."
"""

import view_all_books
from save_all_books import save_all_books
import load_books
import add_books
import book_update
import book_remove
import lend_book
import return_book
from datetime import datetime

all_books = load_books.load_books()

while True:
    print("Welcome to Library Management System")
    print("0. Exit")
    print("1. Add Books")
    print("2. View All Books")
    print("3. Book Update")
    print("4. Book Remove")
    print("5. Lend Book")
    print("6. Return Book")

    menu = input("Select an option: ")
    action_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    if menu == "0":
        print(f"[{action_time}] Thanks for using Library Management System")
        break
    elif menu == "1":
        all_books = add_books.add_books(all_books)
        save_all_books(all_books)
        print(f"[{action_time}] Book added successfully.")
    elif menu == "2":
        view_all_books.view_all_books(all_books)
        print(f"[{action_time}] Displayed all books.")
    elif menu == "3":
        all_books = book_update.book_update(all_books)
        save_all_books(all_books)
        print(f"[{action_time}] Book updated successfully.")
    elif menu == "4":
        all_books = book_remove.book_remove(all_books)
        save_all_books(all_books)
        print(f"[{action_time}] Book removed successfully.")
    elif menu == "5":
        all_books = lend_book.lend_book(all_books)
        save_all_books(all_books)
        print(f"[{action_time}] Book lent successfully.")
    elif menu == "6":
        all_books = return_book.return_book(all_books)
        save_all_books(all_books)
        print(f"[{action_time}] Book returned successfully.")
    else:
        print(f"[{action_time}] Invalid option. Please try again.")
