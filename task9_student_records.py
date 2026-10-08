# Task 9: Mini Project - Student Record Management System
# Storage: list of dictionaries

students = []


def add_student():
    roll = input("Enter Roll No : ").strip()
    if any(s["roll"] == roll for s in students):
        print("A student with this Roll No already exists.")
        return
    name = input("Enter Name    : ").strip()
    course = input("Enter Course  : ").strip()
    marks = input("Enter Marks   : ").strip()
    students.append({"roll": roll, "name": name, "course": course, "marks": marks})
    print(f"Student '{name}' added successfully.")


def display_students():
    if not students:
        print("No records found.")
        return
    print(f"\n{'Roll':<8}{'Name':<18}{'Course':<18}{'Marks':<6}")
    print("-" * 50)
    for s in students:
        print(f"{s['roll']:<8}{s['name']:<18}{s['course']:<18}{s['marks']:<6}")


def search_student():
    key = input("Enter name to search: ").strip().lower()
    found = [s for s in students if key in s["name"].lower()]
    if found:
        print(f"\n{len(found)} record(s) found:")
        for s in found:
            print(f"  Roll: {s['roll']} | Name: {s['name']} | "
                  f"Course: {s['course']} | Marks: {s['marks']}")
    else:
        print("No student found with that name.")


def delete_student():
    key = input("Enter name of student to delete: ").strip().lower()
    for s in students:
        if s["name"].lower() == key:
            students.remove(s)
            print(f"Record of '{s['name']}' deleted.")
            return
    print("Student not found.")


def main():
    while True:
        print("\n===== STUDENT RECORD MANAGEMENT SYSTEM =====")
        print("1. Add Student")
        print("2. Display All Students")
        print("3. Search Student by Name")
        print("4. Delete Student")
        print("5. Exit")
        choice = input("Enter your choice (1-5): ").strip()

        if choice == "1":
            add_student()
        elif choice == "2":
            display_students()
        elif choice == "3":
            search_student()
        elif choice == "4":
            delete_student()
        elif choice == "5":
            print("Thank you for using the system. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
