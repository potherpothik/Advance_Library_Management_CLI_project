def book_remove(all_books):
    try:
        isbn = int(input("Enter the ISBN of the book you want to remove: "))
    except ValueError:
        print("Invalid ISBN. Please enter a numeric value.")
        return all_books

    for book in all_books:
        if book["isbn"] == isbn:
            all_books.remove(book)
            print("Book removed successfully!")
            return all_books

    print("Book not found.")
    return all_books
