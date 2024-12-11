# def view_all_books(all_books):
#     if all_books:
#         print("Books in Library:")
#         print("-" * 100)
#         print(f"{'Title':<20} {'Author':<20} {'ISBN':<14} {'Year':<6} {'Price':<6} {'Qty':<4} {'Added':<20} {'Updated':<20}")
#         print("-" * 100)
#         for book in all_books:
#             print(f"{book['title']:<20} {book['author']:<20} {book['isbn']:<14} {book['publish_year']:<6} {book['price']:<6} {book['quantity']:<4} {book.get('add_time', 'N/A'):<20} {book.get('update_time', 'N/A'):<20}")
#     else:
#         print("No books found.")

def view_all_books(all_books):
    if not all_books:
        print("No books found.")
        return

    print("Books in Library:")
    print("-" * 110)
    print(f"{'Title':<20} {'Author':<20} {'ISBN':<14} {'Year':<6} {'Price':<6} {'Qty':<4} {'Added':<20} {'Updated':<20}")
    print("-" * 110)

    for book in all_books:
        # Handle potential None or missing values
        add_time = book.get('add_time', 'N/A') if book.get('add_time') else 'N/A'
        update_time = book.get('update_time', 'N/A') if book.get('update_time') else 'N/A'

        print(f"{book['title']:<20} {book['author']:<20} {book['isbn']:<14} {book['publish_year']:<6} {book['price']:<6} {book['quantity']:<4} {add_time:<20} {update_time:<20}")