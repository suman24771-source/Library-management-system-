

from add_new_book import *
from delete_a_book import *
from dispay_issued_book import *
from display_all_book import *
from issue_a_book import *
from register_a_student import *
from return_a_book import *
from search_for_a_book import *
def main_menu():
    while True:
            print("Welcome to the main menu")
            print("1. Add a new book")
            print("2. Display all books")
            print("3. search for a book")
            print("4. register a student")
            print("5. issues a book")
            print("6. return a book")
            print("7. display issued books")
            print("8. delete a book")
            print("9. exit")

            choice = input("Enter your choice: ")
            if choice == "1":
                add_new_book()
            elif choice == "2":
                display()
            elif choice == "3":
                search()
            elif choice == "4":
                add_new_students()
            elif choice == "5":
                issue()
            elif choice == "6":
                Return()
            elif choice == "7":
                play()
            elif choice == "8":
                delete()
            elif choice == "9":
                print("Thank you for your time")
                break
            else:
                print("Please enter a valid choice")

main_menu()