def view_all_books(all_books):
    if all_books:
        print("Books in Library:")
        print("-" * 70)
        print(f"{'Title':<20} {'Author':<20} {'ISBN':<10} {'Year':<6} {'Price':<6} {'Qty':<4}")
        print("-" * 70)
        for book in all_books:
            print(f"{book['title']:<20} {book['author']:<20} {book['isbn']:<10} {book['publish_year']:<6} {book['price']:<6} {book['quantity']:<4}")
    else:
        print("No books found.")
