from datetime import datetime

def book_update(all_books):
    try:
        isbn = int(input("Enter the ISBN of the book you want to update: "))
    except ValueError:
        print("Invalid ISBN. Please enter a numeric value.")
        return all_books

    for book in all_books:
        if book["isbn"] == isbn:
            print("Leave a field blank to keep the current value.")
            book["title"] = input(f"Title ({book['title']}): ") or book["title"]
            book["author"] = input(f"Author ({book['author']}): ") or book["author"]
            book["publish_year"] = int(input(f"Publish Year ({book['publish_year']}): ") or book["publish_year"])
            book["price"] = int(input(f"Price ({book['price']}): ") or book["price"])
            book["quantity"] = int(input(f"Quantity ({book['quantity']}): ") or book["quantity"])
            book["update_time"] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

            print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Book '{book['title']}' updated successfully.")
            return all_books

    print("Book not found.")
    return all_books