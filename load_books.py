import json

def load_books():
    try:
        with open("all_books.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        print("No saved books found. Starting with an empty library.")
        return []
