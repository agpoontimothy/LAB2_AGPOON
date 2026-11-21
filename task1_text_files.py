FILE_NAME = "students.txt"


def create_file(filename: str) -> None:
    """1. Creates an empty text file."""
    with open(filename, "w", encoding="utf-8"):
        pass
    print(f"File '{filename}' created successfully.")


def write_initial_records(filename: str, header: str, records: list[str]) -> None:
    """2. Writes the header and initial student records into the file."""
    with open(filename, "w", encoding="utf-8") as file:
        file.write(header + "\n")
        for record in records:
            file.write(record + "\n")
    print(f"Wrote header and {len(records)} student record(s) to '{filename}'.")


def read_records(filename: str, title: str = "Contents") -> None:
    """3. Reads and displays the contents of the file."""
    print(f"\n{title} of '{filename}':")
    print("-" * 45)
    try:
        with open(filename, "r", encoding="utf-8") as file:
            content = file.read()
            if content:
                print(content, end="")
            else:
                print("(File is empty)")
    except FileNotFoundError:
        print(f"Error: '{filename}' was not found.")
    print("-" * 45)


def append_records(filename: str, new_records: list[str]) -> None:
    """4. Appends additional student records without overwriting existing data."""
    with open(filename, "a", encoding="utf-8") as file:
        for record in new_records:
            file.write(record + "\n")
    print(f"Appended {len(new_records)} new record(s) to '{filename}'.")


def main() -> None:
    header = "Student ID,Name,Course"

    initial_students = [
        "2024105146,Timothy Agpoon,BS CpE",
        "2024123456,Cholo Mendoza,BS CpE",
        "2023201234,Rigil Delos Reyes,BS CpE",
    ]

    additional_students = [
        "2024134764,Jericho Matondo,BS CpE",
        "2024103432,Lei San Juan,BS CpE",
    ]

    create_file(FILE_NAME)

    write_initial_records(FILE_NAME, header, initial_students)

    read_records(FILE_NAME, title="Initial Contents")

    append_records(FILE_NAME, additional_students)
    read_records(FILE_NAME, title="Updated Contents")


if __name__ == "__main__":
    main()