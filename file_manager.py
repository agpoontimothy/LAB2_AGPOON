import json
from pathlib import Path

DEFAULT_DATA_FILE = "students_data.json"


def load_students(filepath: str = DEFAULT_DATA_FILE) -> list[dict]:
    """Automatically load student records from JSON; return empty list if missing."""
    path = Path(filepath)
    if not path.exists():
        return []

    try:
        with path.open("r", encoding="utf-8") as file:
            data = json.load(file)
            if isinstance(data, list):
                return data
            print(f"[Warning] Unexpected format in '{filepath}'. Starting with empty records.")
            return []
    except json.JSONDecodeError:
        print(f"[Error] '{filepath}' is corrupted. Starting with empty records.")
        return []
    except OSError as e:
        print(f"[Error] Could not read '{filepath}': {e}")
        return []


def save_students(students: list[dict], filepath: str = DEFAULT_DATA_FILE) -> bool:
    """Save student records to JSON with error handling."""
    path = Path(filepath)
    try:
        with path.open("w", encoding="utf-8") as file:
            json.dump(students, file, indent=4)
        return True
    except OSError as e:
        print(f"[Error] Failed to save records to '{filepath}': {e}")
        return False