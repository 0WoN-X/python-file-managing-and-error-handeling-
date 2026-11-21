
class ZeroDivisionCustomError(Exception):
    pass

try:
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    if num2 == 0:
        raise ZeroDivisionCustomError("Division by zero is not allowed!")

    result = num1 / num2

    print("Result:", result)

except ZeroDivisionCustomError as e:
    print("Error:", e)
