import json
def search():
    a=input("enter book id you want to search: ")
    with open("new_books.json","r") as f:
        books=json.load(f)
    print(books[a])
