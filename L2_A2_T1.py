class InvalidGradeError(Exception):
    """Custom exception raised when a grade is outside the valid range."""
    pass


def get_valid_grade(prompt: str = "Enter a grade (0-100): ") -> float:
    while True:
        raw_input = input(prompt).strip()
        try:
            grade = float(raw_input)

            # Reject NaN or infinity edge cases
            if grade != grade or grade in (float("inf"), float("-inf")):
                raise InvalidGradeError("Grade must be a finite number.")

            if not (0 <= grade <= 100):
                raise InvalidGradeError(
                    f"Invalid range ({grade}): Grades must be between 0 and 100."
                )

            return grade

        except ValueError:
            print(f"Error: '{raw_input}' is not a valid number. Please enter a numeric grade.")
        except InvalidGradeError as e:
            print(f"Error: {e}")


def main():
    grades = []
    print("=== Grade Entry System ===")
    print("Type 'done' when you finish entering grades.\n")

    while True:
        user_entry = input("Enter grade (or 'done' to finish): ").strip()
        if user_entry.lower() == "done":
            break

        try:
            grade = float(user_entry)
            if grade != grade or grade in (float("inf"), float("-inf")):
                raise InvalidGradeError("Grade cannot be NaN or infinite.")
            if not (0 <= grade <= 100):
                raise InvalidGradeError(
                    f"Out-of-range grade ({grade}). Enter a value from 0 to 100."
                )
            grades.append(grade)
            print(f"Recorded grade: {grade:.2f}\n")

        except ValueError:
            print(f"Error: '{user_entry}' is invalid. Enter a number or 'done'.\n")
        except InvalidGradeError as e:
            print(f"Custom Error: {e}\n")

    if grades:
        average = sum(grades) / len(grades)
        print("\n=== Summary ===")
        print(f"Grades entered ({len(grades)}): {grades}")
        print(f"Average grade: {average:.2f}")
    else:
        print("\nNo valid grades were recorded.")


if __name__ == "__main__":
    main()