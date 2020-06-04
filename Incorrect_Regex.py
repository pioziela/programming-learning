def getting_data():
    """
    The function retrieves data from a file. The first line contains information about
    the number of regular expressions. The following lines contain regular expressions.
    """
    with open('incorrect_regex_data.txt', "r") as file_with_data:
        strings_number = int(file_with_data.readline())
        list_with_regexes = []
        for line_number in range(strings_number):
            list_with_regexes.append(file_with_data.readline())
    return strings_number, list_with_regexes


regex_number, regexes_list = getting_data()

lowercase = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'r', 's', 't', 'u', 'v', 'x', 'y', 'z']
uppercase = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','R','S','T','U','V','X','Y','Z']
numbers = ['0','1','2','3','4','5','6','7','8','9']
functions_response = []


def star_plus_check(regexes):
    """
    The function checks the correctness of using the plus sign and the star sign.
    """
    response_list = []
    for regex in regexes:
        counter = 0
        for i, sign in enumerate(regex):
            if i < len(regex) - 1:
                if (regex[i] == '*' or regex[i] == '+') and \
                        (regex[i+1] == '*' or regex[i+1] == '+'):
                    pass
                    counter += 1
                    response_list.append(False)
        if counter == 0:
            response_list.append(True)
    return response_list


def dash_chcek(regexes):
    """
    The function checks if the right characters appear on both sides of the dash.
    It means:
    - lowercase letters in the correct order
    - uppercase letters in the correct order
    - numbers in the correct order.
    """
    response_list = []
    for regex in regexes:
        counter = 0
        for i, sign in enumerate(regex):
            if sign == '-':
                earlier_sign = regex[i - 1]
                later_sign = regex[i + 1]
                if lowercase.count(earlier_sign) == 1 and lowercase.count(later_sign) == 1:
                    if lowercase.index(earlier_sign) < lowercase.index(later_sign):
                        counter += 0
                    else:
                        counter += 1
                elif uppercase.count(earlier_sign) == 1 and uppercase.count(later_sign) == 1:
                    if uppercase.index(earlier_sign) < uppercase.index(later_sign):
                        counter += 0
                    else:
                        counter += 1
                elif numbers.count(earlier_sign) == 1 and numbers.count(later_sign) == 1:
                    if numbers.index(earlier_sign) < numbers.index(later_sign):
                        counter += 0
                    else:
                        counter += 1
                else:
                    pass
                    counter +=1
        if counter == 0:
            response_list.append(True)
        else:
            response_list.append(False)
    return response_list


def square_brackets_check(regexes):
    """
    The function checks if all square brackets are closed.
    """
    response_list = []
    for regex in regexes:
        brackets_indexes_check = []
        left_brackets_indexes = []
        right_brackets_indexes = []
        left_brackets_number = regex.count('[')
        right_brackets_number = regex.count(']')
        if left_brackets_number == right_brackets_number:
            for i, sign in enumerate(regex):
                if sign == '[':
                    left_brackets_indexes.append(i)
                if sign == ']':
                    right_brackets_indexes.append(i)
            for k in range(len(left_brackets_indexes)):
                if left_brackets_indexes[k] < right_brackets_indexes[k]:
                    brackets_indexes_check.append(True)
                else:
                    brackets_indexes_check.append(False)
            if brackets_indexes_check.count(False) != 0:
                response_list.append(False)
            else:
                response_list.append(True)
        else:
            response_list.append(False)
    return response_list


def brackets_check(regexes):
    """
    The function checks if all simple brackets are closed.
    """
    response_list = []
    for regex in regexes:
        brackets_indexes_check = []
        left_brackets_indexes = []
        right_brackets_indexes = []
        left_brackets_number = regex.count('(')
        right_brackets_number = regex.count(')')
        if left_brackets_number == right_brackets_number:
            for i, sign in enumerate(regex):
                if sign == '(':
                    left_brackets_indexes.append(i)
                if sign == ')':
                    right_brackets_indexes.append(i)
            for k in range(len(left_brackets_indexes)):
                if left_brackets_indexes[k] < right_brackets_indexes[k]:
                    brackets_indexes_check.append(True)
                else:
                    brackets_indexes_check.append(False)
            if brackets_indexes_check.count(False) != 0:
                response_list.append(False)
            else:
                response_list.append(True)
        else:
            response_list.append(False)
    return response_list


def regexes_check(*all_functions):
    """
    The function checks which regular expression has no errors.
    And it prints True for a valid expression and False for an invalid expression.
    """
    i = 0
    while i < len(all_functions[0]):
        counter = 0
        for function_response in all_functions:
            if function_response[i] is True:
                counter += 1
        if counter == len(all_functions):
            print(True)
        else:
            print(False)
        i += 1
            

regexes_check(star_plus_check(regexes_list),dash_chcek(regexes_list),square_brackets_check(regexes_list),brackets_check(regexes_list))
