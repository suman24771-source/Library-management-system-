
import json
import os
add="new_student.json"

def load():
    if os.path.exists(add):
        with open("new_students.json", "r") as f:
            try:
                return json.load(f)
            except json.JSONDecodeError:
               return {}
    else:
        return {}
def save(new_students):
   with open(add, "w") as f:
       json.dump(new_students, f,indent=4)
def add_new_students():
    data=load()
    a=input("enter new student id: ")
    b=input("enter student name: ")
    c=input("enter branch: ")
    d=input("enter student semester: ")
    data[a]={
            "name":b,
            "branch":c,
            "semester":d
        }
    save(data)
    print("new student added")
