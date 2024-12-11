import json

def save_all_books(all_books):
    with open("all_books.json", "w") as file:
        json.dump(all_books, file, indent=4)
