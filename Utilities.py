import math
from typing import Any, Iterable, Optional


def calculate_average(scores: Iterable[float]) -> float:
    """Return the arithmetic mean of a non-empty list of finite grades."""
    values = list(scores)
    if not values:
        raise ValueError("Cannot compute average from an empty grade list.")

    cleaned: list[float] = []
    for item in values:
        num = float(item)
        if math.isnan(num) or math.isinf(num):
            raise ValueError("Grades must be finite numbers.")
        cleaned.append(num)

    return sum(cleaned) / len(cleaned)


def evaluate_grade(average: float) -> dict[str, str]:
    """Evaluate a 0-100 average into a letter grade, standing, and remarks."""
    num = float(average)
    if math.isnan(num) or math.isinf(num) or not (0.0 <= num <= 100.0):
        raise ValueError("Average must be a finite number between 0 and 100.")

    if num >= 90.0:
        letter, standing, remarks = "A", "Passed", "Excellent"
    elif num >= 85.0:
        letter, standing, remarks = "B+", "Passed", "Very Good"
    elif num >= 80.0:
        letter, standing, remarks = "B", "Passed", "Good"
    elif num >= 75.0:
        letter, standing, remarks = "C", "Passed", "Satisfactory"
    elif num >= 60.0:
        letter, standing, standing_or_remarks = "D", "Conditional", "Needs Improvement"
        remarks = standing_or_remarks
    else:
        letter, standing, remarks = "F", "Failed", "Failed"

    return {
        "average": f"{num:.2f}",
        "letter": letter,
        "standing": standing,
        "remarks": remarks,
    }


def _extract_fields(
    record_or_id: Any,
    name: Optional[str],
    program: Optional[str],
    scores: Optional[Iterable[float]],
) -> tuple[str, str, str, list[float]]:
    """Support Student objects, dicts, or direct arguments uniformly."""
    if hasattr(record_or_id, "student_id") and hasattr(record_or_id, "name"):
        s_id = str(record_or_id.student_id)
        s_name = str(record_or_id.name)
        s_program = str(getattr(record_or_id, "program", program or "N/A"))
        raw_scores = getattr(record_or_id, "scores", getattr(record_or_id, "grades", scores))
        return s_id, s_name, s_program, list(raw_scores) if raw_scores is not None else []

    if isinstance(record_or_id, dict):
        s_id = str(record_or_id.get("student_id", record_or_id.get("id", "N/A")))
        s_name = str(record_or_id.get("name", "N/A"))
        s_program = str(record_or_id.get("program", program or "N/A"))
        raw_scores = record_or_id.get("scores", record_or_id.get("grades", scores))
        return s_id, s_name, s_program, list(raw_scores) if raw_scores is not None else []

    return (
        str(record_or_id),
        str(name or "N/A"),
        str(program or "N/A"),
        list(scores) if scores is not None else [],
    )


def display_student_info(
    record_or_id: Any,
    name: Optional[str] = None,
    program: Optional[str] = None,
    scores: Optional[Iterable[float]] = None,
) -> str:
    """Format and display a student's details, average, and grade evaluation."""
    s_id, s_name, s_program, score_list = _extract_fields(record_or_id, name, program, scores)

    lines = [
        "-" * 42,
        f"ID         : {s_id}",
        f"Name       : {s_name}",
        f"Program    : {s_program}",
    ]

    if score_list:
        avg = calculate_average(score_list)
        ev = evaluate_grade(avg)
        formatted = ", ".join(f"{float(s):.2f}" for s in score_list)
        lines.extend([
            f"Grades     : {formatted}",
            f"Average    : {ev['average']}",
            f"Evaluation : {ev['letter']} ({ev['standing']} - {ev['remarks']})",
        ])
    else:
        lines.append("Grades     : None")

    lines.append("-" * 42)
    output = "\n".join(lines)
    print(output)
    return output


def prompt_non_empty(prompt: str) -> str:
    """Prompt until a non-empty string is provided."""
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print("Error: Input cannot be blank.")


def prompt_scores(prompt: str = "Enter grades separated by commas (0-100): ") -> list[float]:
    """Prompt for and validate comma-separated numeric grades between 0 and 100."""
    while True:
        raw = input(prompt).strip()
        if not raw:
            print("Error: Please enter at least one grade.")
            continue

        try:
            parts = [p.strip() for p in raw.split(",") if p.strip()]
            if not parts:
                raise ValueError("No valid grades entered.")

            scores: list[float] = []
            for part in parts:
                val = float(part)
                if math.isnan(val) or math.isinf(val) or not (0.0 <= val <= 100.0):
                    raise ValueError(f"'{val}' is outside the 0-100 range.")
                scores.append(val)
            return scores

        except ValueError as exc:
            print(f"Invalid grade input: {exc}")


def build_summary_report(records: list[Any]) -> str:
    """Build a formatted summary report for a list of student records."""
    if not records:
        return "\n=== SUMMARY REPORT ===\nNo student records found.\n"

    averages: list[float] = []
    for rec in records:
        _, _, _, rec_scores = _extract_fields(rec, None, None, None)
        if rec_scores:
            averages.append(calculate_average(rec_scores))

    lines = [
        "\n" + "=" * 42,
        "STUDENT SUMMARY REPORT",
        "=" * 42,
        f"Total Students : {len(records)}",
    ]

    if averages:
        class_avg = calculate_average(averages)
        class_ev = evaluate_grade(class_avg)
        lines.extend([
            f"Graded Students: {len(averages)}",
            f"Highest Avg    : {max(averages):.2f}",
            f"Lowest Avg     : {min(averages):.2f}",
            f"Class Average  : {class_avg:.2f} ({class_ev['letter']} - {class_ev['standing']})",
        ])
    else:
        lines.append("Class Average  : N/A")

    lines.append("=" * 42)
    return "\n".join(lines)