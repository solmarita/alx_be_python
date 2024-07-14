def safe_divide(numerator, denominator):
    "Safely carries out divisions account for zero division errors"

    try:
        numerator, denominator = float(numerator), float(denominator)
        return f"The result of the division is {float(numerator/denominator)}"

    except ZeroDivisionError:
        return "Error: Cannot divide by zero."
    except ValueError:
        return "Error: Please enter numeric values only."