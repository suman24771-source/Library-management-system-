
import json
import os


def issue():
    
    book_id = input("Enter book ID you want to issue: ").strip()
    student_id = input("Enter student ID: ").strip()

    
    if os.path.exists("new_books.json"):
        with open("new_books.json", "r") as f:
            books = json.load(f)
    else:
        print("Error: new_books.json not found.")
        return

    
    if os.path.exists("new_student.json"):
        with open("new_student.json", "r") as f:
            students = json.load(f)
    else:
        print("Error: new_students.json not found.")
        return

    
    issued_file = "issued_books.json"
    if os.path.exists(issued_file):
        with open(issued_file, "r") as f:
            try:
                issued = json.load(f)
            except json.JSONDecodeError:
                issued = {}
    else:
        issued = {}

    
    if book_id in books:
        if student_id in students:
            
            if books[book_id].get("copies", 0) != 0:
                
                books[book_id]["copies"] =int( books[book_id]["copies"]) - 1

                
                student_info = students[student_id]

                
                issued[book_id] = {
                    "student id": student_id,
                    "student name": student_info.get("name", "N/A"),
                    "student branch": student_info.get("branch", "N/A"),
                    "semester": student_info.get("semester", "N/A")
                }

                
                with open("new_books.json", "w") as f:
                    json.dump(books, f, indent=4)

                
                with open(issued_file, "w") as f:
                    json.dump(issued, f, indent=4)

                print("Book successfully issued!")
            else:
                print("Copies are not available.")
        else:
            print("Student ID not found.")
    else:
        print("Book not found.")

