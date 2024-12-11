def add_books(all_books):
    title = input("Enter book title: ")
    author = input("Enter book author: ")
    try:
        isbn = int(input("Enter book ISBN: "))
        publish_year = int(input("Enter book publish year: "))
        price = int(input("Enter book price: "))
        quantity = int(input("Enter book quantity: "))
    except ValueError:
        print("Invalid input. Please enter numeric values for ISBN, year, price, and quantity.")
        return all_books

    for book in all_books:
        if book["isbn"] == isbn:
            print("Book with this ISBN already exists.")
            return all_books

    book = {
        "title": title,
        "author": author,
        "isbn": isbn,
        "publish_year": publish_year,
        "price": price,
        "quantity": quantity
    }

    all_books.append(book)
    print("Book added successfully!")
    return all_books
