import csv
from pathlib import Path

CSV_FILE = "students.csv"


def create_and_populate_csv(path: Path) -> None:
    headers = ["Student ID", "Name", "Course"]
    students = [
        ["2024105146", "Timothy Agpoon", "BS CpE"],
        ["2024123456", "Cholo Mendoza", "BS CpE"],
        ["2023201234", "Rigil Delos Reyes", "BS CpE"],
        ["2024134764", "Jericho Matondo", "BS CpE"],
        ["2024103432", "Lei San Juan", "BS CpE"],
    ]

    with path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(headers)
        writer.writerows(students)

    print(f"Created '{path.name}' with {len(students)} student records.")


def read_and_display_table(path: Path) -> None:
    with path.open("r", newline="", encoding="utf-8") as f:
        reader = csv.reader(f)
        rows = list(reader)

    if not rows:
        print("CSV file is empty.")
        return

    col_widths = [
        max(len(str(row[i])) for row in rows)
        for i in range(len(rows[0]))
    ]

    def format_row(row: list[str]) -> str:
        return "| " + " | ".join(str(val).ljust(col_widths[i]) for i, val in enumerate(row)) + " |"

    separator = "+-" + "-+-".join("-" * w for w in col_widths) + "-+"

    print(f"\nStudent Records from '{path.name}':")
    print(separator)
    print(format_row(rows[0]))
    print(separator)
    for row in rows[1:]:
        print(format_row(row))
    print(separator)


def main() -> None:
    csv_path = Path(CSV_FILE)
    create_and_populate_csv(csv_path)
    read_and_display_table(csv_path)


if __name__ == "__main__":
    main()