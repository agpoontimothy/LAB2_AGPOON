from file_manager import load_students, save_students
from Utilities import (
    build_summary_report,
    display_student_info,
    prompt_non_empty,
    prompt_scores,
)


def find_student(students: list[dict], student_id: str) -> dict | None:
    """Return a matching student record by ID (case-insensitive), or None."""
    target = student_id.strip().lower()
    for student in students:
        if str(student.get("student_id", "")).lower() == target:
            return student
    return None


def add_student(students: list[dict]) -> None:
    student_id = prompt_non_empty("Enter Student ID: ")
    if find_student(students, student_id):
        print(f"Error: Student ID '{student_id}' already exists.")
        return

    name = prompt_non_empty("Enter Student Name: ")
    program = prompt_non_empty("Enter Program: ")
    scores = prompt_scores()

    students.append({
        "student_id": student_id,
        "name": name,
        "program": program,
        "scores": scores,
    })
    save_students(students)
    print(f"Added and saved student '{name}'.")


def view_students(students: list[dict]) -> None:
    if not students:
        print("\nNo student records to display.")
        return

    for student in students:
        display_student_info(student)


def search_student(students: list[dict]) -> None:
    student_id = prompt_non_empty("Enter Student ID to search: ")
    student = find_student(students, student_id)
    if not student:
        print(f"No student found with ID '{student_id}'.")
        return

    display_student_info(student)


def update_student(students: list[dict]) -> None:
    student_id = prompt_non_empty("Enter Student ID to update: ")
    student = find_student(students, student_id)
    if not student:
        print(f"No student found with ID '{student_id}'.")
        return

    print(f"Updating record for {student['name']} ({student['student_id']}).")
    student["name"] = prompt_non_empty(f"New Name [{student['name']}]: ")
    student["program"] = prompt_non_empty(f"New Program [{student['program']}]: ")
    student["scores"] = prompt_scores("Enter updated grades (comma-separated): ")

    save_students(students)
    print("Student record updated and saved.")


def delete_student(students: list[dict]) -> None:
    student_id = prompt_non_empty("Enter Student ID to delete: ")
    student = find_student(students, student_id)
    if not student:
        print(f"No student found with ID '{student_id}'.")
        return

    students.remove(student)
    save_students(students)
    print(f"Deleted student '{student['name']}' and updated saved records.")


def main() -> None:
    students = load_students()
    print(f"Loaded {len(students)} student record(s).")

    while True:
        print("\n=== STUDENT MANAGEMENT SYSTEM ===")
        print("1. Add Student")
        print("2. View All Students")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Summary Report")
        print("7. Save & Exit")

        choice = input("Choose an option (1-7): ").strip()

        try:
            if choice == "1":
                add_student(students)
            elif choice == "2":
                view_students(students)
            elif choice == "3":
                search_student(students)
            elif choice == "4":
                update_student(students)
            elif choice == "5":
                delete_student(students)
            elif choice == "6":
                print(build_summary_report(students))
            elif choice == "7":
                if save_students(students):
                    print("Records saved. Exiting program.")
                break
            else:
                print("Invalid choice. Enter a number from 1 to 7.")
        except Exception as exc:
            print(f"[Unexpected Error] {type(exc).__name__}: {exc}")


if __name__ == "__main__":
    main()