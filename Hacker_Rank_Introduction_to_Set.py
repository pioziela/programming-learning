# Determining the average value of a set of unique integers.
def getting_integers():
    """
    The function getting_integers downloads a file in which the first line contains number
    that specify the number of not unique and unsorted integers in second line.
    Finally the function sorts numbers.
    """
    with open('Set_of_integers_to_Introduction_to_Set.txt', "r") as file_with_data:
        number_of_numbers = int(file_with_data.readline())
        set_of_integers = list(map(int, file_with_data.readline().rstrip().split()))
        set_of_integers.sort()
    return set_of_integers


def set_of_unique_integers(integers_set):
    """
    The function set_of_unique_integers create and return list of unique integers.
    """
    list_of_unique_numbers = []
    for index in range(len(integers_set)):
        if index == 0:
            list_of_unique_numbers.append(integers_set[index])
        elif integers_set[index] != integers_set[index - 1]:
            list_of_unique_numbers.append(integers_set[index])
    return list_of_unique_numbers


def average_of_unique_integers(unique_integers):
    """
    The function average_of_unique_integers return average of unique integers.
    """
    average = sum(unique_integers) / len(unique_integers)
    return average


print(average_of_unique_integers(set_of_unique_integers(getting_integers())))
