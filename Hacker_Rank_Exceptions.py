import sys


def divide_exceptions():
    """
    divide_exceptions function trying to divide two values.
    The user provides data in the following format:
    - in the first line the number of divisions to be carried out,
    - in the following lines, the user provides two values to divide, the values should be separated by a space.
    The function returns a division result or a corresponding error.
    """
    line_number = 0
    number_of_lines = int(sys.stdin.readline())
    while line_number < number_of_lines:
        numbers_to_divide = list(map(str, sys.stdin.readline().rstrip().split()))
        try:
            print(int(numbers_to_divide[0]) / int(numbers_to_divide[1]))
        except ZeroDivisionError:
            print("Error Code: integer division or modulo by zero")
        except ValueError as invalid_literal:
            error = f"Error Code: {invalid_literal}"
            print(error)
        line_number += 1


divide_exceptions()
