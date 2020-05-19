def getting_integers():
    """
    The function getting_integers downloading from the file list of integers to sort.
    """
    with open('bubble_sort_table.txt', "r") as text:
        text_in_file = text.read()
        table_numbers = list(map(int, text_in_file.rstrip().split()))
        return table_numbers


def count_swaps(numbers_to_sort):
    """
    The function count_swaps sorting numbers in the list by bubble sorting.
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
    return number_of_swaps, first_element, last_element


swaps_number, first_el, last_el = count_swaps(getting_integers())


def printing_results():
    print('Array is sorted in', swaps_number, 'swaps.', end='\n')
    print('First Element:', first_el)
    print('Last Element:', last_el)


printing_results()