import json

def save_all_books(all_books):
    with open("all_books.json", "w") as file:
        json.dump(all_books, file, indent=4)

# Updated view_all_books.py
def view_all_books(all_books):
    if all_books:
        print("Books in Library:")
        print("-" * 100)
        print(f"{'Title':<20} {'Author':<20} {'ISBN':<14} {'Year':<6} {'Price':<6} {'Qty':<4} {'Added':<20} {'Updated':<20}")
        print("-" * 100)
        for book in all_books:
            add_time = book.get('add_time', 'N/A') or 'N/A'
            update_time = book.get('update_time', 'N/A') or 'N/A'
            print(f"{book['title']:<20} {book['author']:<20} {book['isbn']:<14} {book['publish_year']:<6} {book['price']:<6} {book['quantity']:<4} {add_time:<20} {update_time:<20}")
    else:
        print("No books found.")