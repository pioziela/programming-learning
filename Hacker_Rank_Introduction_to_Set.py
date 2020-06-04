# Determining the average value of a set of unique integers.
def getting_integers():
    """
    The function getting_integers downloads a file in which the first line contains number
    that specify the number of not unique and unsorted integers in second line.
    Finally the function sorts numbers and return list of unique integers.
    """
    with open('Set_of_integers_to_Introduction_to_Set.txt', "r") as file_with_data:
        number_of_numbers = int(file_with_data.readline())
        set_of_integers = list(map(int, file_with_data.readline().rstrip().split()))
        set_of_integers.sort()
    return list(set(set_of_integers))


def average_of_unique_integers(unique_integers):
    """
    The function average_of_unique_integers return average of unique integers.
    """
    try:
        return sum(unique_integers) / len(unique_integers)
    except ZeroDivisionError:
        return "No numbers to calculate the average. Cannot divide by zero."


print(average_of_unique_integers(getting_integers()))
