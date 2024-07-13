def safe_divide(numerator, denominator):
    try:
        num = float(numerator)
        denom = float(denominator)
        result = num / denom
        return result
    except ValueError:
        return "Error: Non-numeric input detected. Please enter numeric values."
    except ZeroDivisionError:
        return "Error: Division by zero is not allowed."
