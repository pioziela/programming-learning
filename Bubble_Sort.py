"""pobranie z pliku listy nieposortowanych liczb:"""
with open('bubble_sort_table.txt', "r") as text:
    text_in_file = text.read()
    table_numbers = list(map(int, text_in_file.rstrip().split()))


def change_element_position(elements, position):
    """Funkcja zmieniająca pozycję dwóch elementów w liście."""
    elements[position], elements[position + 1] = elements[position + 1], elements[position]


def count_swaps(numbers_to_sort):
    """Funkcja sortująca liczby na liście metodą sortowania bąbelkowego."""
    number_of_swaps = 0  # licznik ilości wykonanych zmian pozycji elementów w liście
    for index_1 in range(len(numbers_to_sort)):
        for index_2 in range(len(numbers_to_sort)-1):
            if numbers_to_sort[index_2] > numbers_to_sort[index_2+1]:
                change_element_position(numbers_to_sort, index_2)
                number_of_swaps += 1
    first_element = numbers_to_sort[0]  # pierwszy element w posortowanej liście liczb
    last_element = numbers_to_sort[len(numbers_to_sort) - 1]  # ostatni element w posortowanej liście liczb
    return number_of_swaps, first_element, last_element


swaps_number, first_el, last_el = count_swaps(table_numbers)

print('Array is sorted in', swaps_number, 'swaps.', end='\n')
print('First Element:', first_el)
print('Last Element:', last_el)