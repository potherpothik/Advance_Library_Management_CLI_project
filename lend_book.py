from datetime import datetime
import json


def load_lend_data():
    try:
        with open("lend_books.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_lend_data(lend_data):
    with open("lend_books.json", "w") as file:
        json.dump(lend_data, file, indent=4)

def lend_book(all_books):
    lend_data = load_lend_data()
    book_title = input("Enter the title of the book to lend: ")

    for book in all_books:
        if book["title"].lower() == book_title.lower() and book["quantity"] > 0:
            borrower_name = input("Enter borrower's name: ")
            phone_number = input("Enter borrower's phone number: ")
            due_date = input("Enter return due date (YYYY-MM-DD): ")

            try:
                datetime.strptime(due_date, "%Y-%m-%d")
            except ValueError:
                print("Invalid date format. Please use YYYY-MM-DD.")
                return all_books

            lend_data.append({
                "borrower_name": borrower_name,
                "phone_number": phone_number,
                "book_title": book["title"],
                "due_date": due_date
            })
            
            book["quantity"] -= 1
            save_lend_data(lend_data)
            print(f"Book '{book['title']}' lent successfully to {borrower_name}.")
            return all_books

    print("Book not available for lending or not found.")
    return all_books
