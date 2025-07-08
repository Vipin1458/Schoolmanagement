
from auth import login
from student import register_student, list_students

def main():
    print("Welcome to School Management System")
    if not login():
        return

    while True:
        print("\nMenu:")
        print("1. Register Student")
        print("2. List Students")
        print("3. Exit")
      

        choice = input("Choose: ")

        if choice == "1":
            register_student()
        elif choice == "2":
            list_students()
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid option.")

if __name__ == "__main__":
    main()
