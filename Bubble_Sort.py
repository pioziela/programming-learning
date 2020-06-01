def getting_integers():
    """
    Downloading from the file list of integers to sort.
    """
    with open('bubble_sort_table.txt', "r") as text:
        text_in_file = text.read()
        table_numbers = list(map(int, text_in_file.rstrip().split()))
        return table_numbers


def count_swaps(numbers_to_sort):
    """
    Sort numbers in the list by bubble sorting.
    """
    number_of_swaps = 0
    for index_1 in range(len(numbers_to_sort)):
        for index_2 in range(len(numbers_to_sort)-1):
            if numbers_to_sort[index_2] > numbers_to_sort[index_2+1]:
                numbers_to_sort[index_2], numbers_to_sort[index_2 + 1] =\
                    numbers_to_sort[index_2 + 1], numbers_to_sort[index_2]
                number_of_swaps += 1
    first_element = numbers_to_sort[0]
    last_element = numbers_to_sort[len(numbers_to_sort) - 1]
    return print('Array is sorted in', number_of_swaps, 'swaps.'), print('First Element:', first_element), print('Last Element:', last_element)


count_swaps(getting_integers())