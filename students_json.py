import json

JSON_FILE = "students.json"


def create_and_store_students(filename: str, students: list[dict[str, str]]) -> None:
    """1. Creates a JSON file and 2. stores student information."""
    payload = {"students": students}
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(payload, file, indent=4)
    print(f"Created '{filename}' and stored {len(students)} student record(s).")


def read_and_display_students(filename: str) -> None:
    """3. Reads data from the JSON file and 4. displays formatted output."""
    try:
        with open(filename, "r", encoding="utf-8") as file:
            data = json.load(file)
    except FileNotFoundError:
        print(f"Error: '{filename}' was not found.")
        return
    except json.JSONDecodeError:
        print(f"Error: '{filename}' contains invalid JSON.")
        return

    students = data.get("students", [])
    print("\nFormatted Student Records:")
    print(f"{'Student ID':<14} {'Name':<22} {'Course':<10}")
    print("-" * 48)
    for student in students:
        print(
            f"{student.get('student_id', ''):<14} "
            f"{student.get('name', ''):<22} "
            f"{student.get('course', ''):<10}"
        )
    print("-" * 48)


def main() -> None:
    student_records = [
        {"student_id": "2024105146", "name": "Timothy Agpoon", "course": "BS CpE"},
        {"student_id": "2024123456", "name": "Cholo Mendoza", "course": "BS CpE"},
        {"student_id": "2023201234", "name": "Rigil Delos Reyes", "course": "BS CpE"},
        {"student_id": "2024134764", "name": "Jericho Matondo", "course": "BS CpE"},
        {"student_id": "2024103432", "name": "Lei San Juan", "course": "BS CpE"},
    ]

    create_and_store_students(JSON_FILE, student_records)
    read_and_display_students(JSON_FILE)


if __name__ == "__main__":
    main()