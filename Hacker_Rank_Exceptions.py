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
    number_of_lines = 0
    error_messages = []
    while line_number <= number_of_lines:
            line = sys.stdin.readline()
            if line_number == 0:
                number_of_lines = int(line)
            elif 0 < line_number <= number_of_lines:
                numbers_to_divide = list(map(str, line.rstrip().split()))
                try:
                    error_messages.append(int(int(numbers_to_divide[0]) / int(numbers_to_divide[1])))
                except ZeroDivisionError:
                    error_messages.append("Error Code: integer division or modulo by zero")
                except ValueError as invalid_literal:
                    error = "Error Code:" + ' ' + str(invalid_literal)
                    error_messages.append(error)
            line_number += 1
    return error_messages


def printing_exceptions(exceptions_list):
    for index in exceptions_list:
        print(index)


printing_exceptions(divide_exceptions())
