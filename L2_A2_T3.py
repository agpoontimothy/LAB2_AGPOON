import math


def calculate(num1: float, operator: str, num2: float) -> float:
    """Performs basic arithmetic and raises appropriate errors for invalid operations."""
    if operator == "+":
        result = num1 + num2
    elif operator == "-":
        result = num1 - num2
    elif operator == "*":
        result = num1 * num2
    elif operator == "/":
        if num2 == 0:
            raise ZeroDivisionError("Cannot divide by zero.")
        result = num1 / num2
    elif operator in ("**", "^"):
        if num1 == 0 and num2 < 0:
            raise ZeroDivisionError("Cannot raise zero to a negative power.")
        result = num1 ** num2
    else:
        raise ValueError(f"Unsupported operator '{operator}'. Use +, -, *, /, or **.")

    if math.isnan(result) or math.isinf(result):
        raise OverflowError("Calculation resulted in an overflow or undefined value.")

    return result


def main():
    print("=== Exception-Safe Calculator ===")
    print("Supported operators: +, -, *, /, ** (power)")
    print("Type 'quit' at any prompt to exit.\n")

    while True:
        try:
            first_raw = input("Enter first number: ").strip()
            if first_raw.lower() == "quit":
                break
            num1 = float(first_raw)
            if math.isnan(num1) or math.isinf(num1):
                raise ValueError("Input must be a finite number.")

            operator = input("Enter operator (+, -, *, /, **): ").strip()
            if operator.lower() == "quit":
                break

            second_raw = input("Enter second number: ").strip()
            if second_raw.lower() == "quit":
                break
            num2 = float(second_raw)
            if math.isnan(num2) or math.isinf(num2):
                raise ValueError("Input must be a finite number.")

            outcome = calculate(num1, operator, num2)
            print(f"Result: {num1} {operator} {num2} = {outcome}\n")

        except ValueError as e:
            print(f"[ValueError] Invalid input or operator: {e}\n")
        except ZeroDivisionError as e:
            print(f"[ZeroDivisionError] Math error: {e}\n")
        except Exception as e:
            print(f"[Unexpected Error] {type(e).__name__}: {e}\n")

    print("Calculator closed.")


if __name__ == "__main__":
    main()