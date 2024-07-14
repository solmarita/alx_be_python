def safe_divide(numerator, denominator):
    "Safely carries out divisions account for zero division errors"

    try:
        numerator, denominator = float(numerator), float(denominator)
        return f"The result of this division is {float(numerator/denominator)}"

    except ZeroDivisionError:
        return "Can't divide by zero!"
    except ValueError:
        return "Make sure to enter numerical values"