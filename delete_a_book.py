import json
def delete():

    a=input("enter book id you want to delete: ")
    with open("new_books.json","r") as f:
        data=json.load(f)
    if a in data:
        data.pop(a)
        with open("new_books.json","w") as f:
            json.dump(data,f,indent=4)
        print("book deleted")
    else:
        print("book not found")
