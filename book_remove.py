from datetime import datetime

def book_remove(all_books):
    try:
        isbn = int(input("Enter the ISBN of the book you want to remove: "))
    except ValueError:
        print("Invalid ISBN. Please enter a numeric value.")
        return all_books

    for book in all_books:
        if book["isbn"] == isbn:
            print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Book '{book['title']}' removed successfully.")
            all_books.remove(book)
            return all_books

    print("Book not found.")
    return all_books