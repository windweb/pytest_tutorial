def add(num1, num2):
    return num1 + num2


def divide(num1, num2):
    if 0 == num2:
        raise ValueError("Cannot divide by zero")
    return num1 / num2
