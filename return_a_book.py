import json
def Return():
    a=input("Enter a book id: ")
    with open("issued_books.json","r") as f:
        books = json.load(f)
        if a in books:
            books.pop(a)
            print("book returned successfully")
            with open("issued_books.json","w") as f:
                json.dump(books,f)

        else:
            print("book not found")
