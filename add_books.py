import random
from datetime import datetime

def add_books(all_books):
    title = input("Enter book title: ")
    author = input("Enter book author: ")
    try:
        isbn = random.randint(1000000000000, 9999999999999)
        publish_year = int(input("Enter book publish year: "))
        price = int(input("Enter book price: "))
        quantity = int(input("Enter book quantity: "))
    except ValueError:
        print("Invalid input. Please enter numeric values for year, price, and quantity.")
        return all_books

    book = {
        "title": title,
        "author": author,
        "isbn": isbn,
        "publish_year": publish_year,
        "price": price,
        "quantity": quantity,
        "add_time": datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        "update_time": None
    }

    all_books.append(book)
    print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Book '{title}' added with ISBN {isbn}.")
    return all_books