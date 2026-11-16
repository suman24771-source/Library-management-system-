import json
import os
add="new_books.json"

def load():
    if os.path.exists(add):
        with open("new_books.json", "r") as f:
            try:
                return json.load(f)
            except json.JSONDecodeError:
               return {}
    else:
        return {}
def save(new_book):
   with open(add, "w") as f:
       json.dump(new_book, f,indent=4)
def add_new_book():
    data=load()
    a=input("enter new book id: ")
    b=input("enter new book title: ")
    c=input("enter new book author: ")
    d=input("enter available copies: ")
    data[a]={
            "title":b,
            "author":c,
            "copies":d
        }
    save(data)
    print("new book added")
