import json
import os

FILE = "library.json"

def load_data():
    if not os.path.exists(FILE):
        return {
            "books": [],
            "members": [],
            "transactions": []
        }

    with open(FILE, "r") as file:
        return json.load(file)


def save_data(data):
    with open(FILE, "w") as file:
        json.dump(data, file, indent=4)


def add_book(title, author, category, quantity):
    data = load_data()

    book = {
        "book_id": max(
            [b["book_id"] for b in data["books"]],
            default=0
        ) + 1,
        "title": title,
        "author": author,
        "category": category,
        "quantity": quantity
    }

    data["books"].append(book)
    save_data(data)


def add_member(name, email):
    data = load_data()

    member = {
        "member_id": max(
            [m["member_id"] for m in data["members"]],
            default=0
        ) + 1,
        "name": name,
        "email": email
    }

    data["members"].append(member)
    save_data(data)