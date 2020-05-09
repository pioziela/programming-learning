with open('bubble_sort_table.txt', "r") as text:
    text_in_file = text.read()
    table_numbers = list(map(int, text_in_file.rstrip().split()))


def count_Swaps(list):
    change = lambda list, index2: list.__setitem__(slice(index2, index2 + 2), (list[index2 + 1], list[index2]))
    swaps_list = [change(list, index2) for index, element in enumerate(list) for index2, element2 in enumerate(list) if index2 < len(list) - 1 and list[index2] > list[index2 + 1]]
    first_element = list[0]
    last_element = list[len(list)-1]
    number_of_swaps = len(swaps_list)
    return number_of_swaps, first_element, last_element


swaps_number, first_el, last_el = count_Swaps(table_numbers)

print('Array is sorted in', swaps_number, 'swaps.', end='\n')
print('First Element:', first_el)
print('Last Element:', last_el)