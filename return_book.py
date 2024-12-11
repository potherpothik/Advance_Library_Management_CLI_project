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

def return_book(all_books):
    lend_data = load_lend_data()
    book_title = input("Enter the title of the book to return: ")
    borrower_name = input("Enter the borrower's name: ")

    for record in lend_data:
        if record["book_title"].lower() == book_title.lower() and record["borrower_name"].lower() == borrower_name.lower():
            lend_data.remove(record)
            
            for book in all_books:
                if book["title"].lower() == book_title.lower():
                    book["quantity"] += 1
                    break

            save_lend_data(lend_data)
            print(f"Book '{book_title}' returned successfully by {borrower_name}.")
            return all_books

    print("No matching lending record found.")
    return all_books