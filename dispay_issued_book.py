import json
def play():
    with open("issued_book.json",'r') as f:
        data=json.load(f)
    print(data)