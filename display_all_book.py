import json
def display():
    with open("new_books.json","r") as f:
        data = json.load(f)
    print(data)
