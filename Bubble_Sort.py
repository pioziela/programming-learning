with open('bubble_sort_table.txt', "r") as text:
    text_in_file = text.read()
    table_numbers = list(map(int, text_in_file.rstrip().split()))

def Count_Swaps(list):
    change = lambda list, index2: list.__setitem__(slice(index2, index2 + 2), (list[index2 + 1], list[index2]))
    swaps_list = [change(list, index2) for index, element in enumerate(list) for index2, element2 in enumerate(list) if index2 < len(list) - 1 and list[index2] > list[index2 + 1]]
    First_Element = list[0]
    Last_Element = list[len(list)-1]
    Number_of_Swaps = len(swaps_list)
    print ('Array is sorted in',Number_of_Swaps, 'swaps.', end='\n')
    print('First Element:',First_Element)
    print('Last Element:', Last_Element)


Count_Swaps(table_numbers)