
import json
import os


def issue():
    # .strip() removes any accidental spaces typed during input
    book_id = input("Enter book ID you want to issue: ").strip()
    student_id = input("Enter student ID: ").strip()

    # 1. Load books file safely
    if os.path.exists("new_books.json"):
        with open("new_books.json", "r") as f:
            books = json.load(f)
    else:
        print("Error: new_books.json not found.")
        return

    # 2. Load students file safely
    if os.path.exists("new_student.json"):
        with open("new_student.json", "r") as f:
            students = json.load(f)
    else:
        print("Error: new_students.json not found.")
        return

    # 3. Load existing issued books (or create empty dict if file is missing/empty)
    issued_file = "issued_books.json"
    if os.path.exists(issued_file):
        with open(issued_file, "r") as f:
            try:
                issued = json.load(f)
            except json.JSONDecodeError:
                issued = {}
    else:
        issued = {}

    # 4. Validation & Processing
    if book_id in books:
        if student_id in students:
            # Check if copies are available
            if books[book_id].get("copies", 0) != 0:
                # Decrement copy count
                books[book_id]["copies"] =int( books[book_id]["copies"]) - 1

                # Fetch student details automatically from the nested dictionary
                student_info = students[student_id]

                # Record the issuance
                issued[book_id] = {
                    "student id": student_id,
                    "student name": student_info.get("name", "N/A"),
                    "student branch": student_info.get("branch", "N/A"),
                    "semester": student_info.get("semester", "N/A")
                }

                # Save updated books back to file
                with open("new_books.json", "w") as f:
                    json.dump(books, f, indent=4)

                # Save updated issued books back to file
                with open(issued_file, "w") as f:
                    json.dump(issued, f, indent=4)

                print("Book successfully issued!")
            else:
                print("Copies are not available.")
        else:
            print("Student ID not found.")
    else:
        print("Book not found.")

