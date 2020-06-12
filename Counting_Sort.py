input_numbers_to_sort = [1, 4, 1, 8, 9, 2, -1, 3, 7, 5, 2, 133, 0, 8, 8, 8]


def counting_sort(numbers_to_sort):
    max_element = max(numbers_to_sort)
    min_element = min(numbers_to_sort)
    elements_and_numbers_of_elements_count = {}
    counter_of_elements = 0
    for i in range(min_element, max_element+1):
        counter_of_elements = counter_of_elements + numbers_to_sort.count(i)
        elements_and_numbers_of_elements_count[i] = counter_of_elements
    output_sort_numbers = []
    counter_decrease = 0
    for key in elements_and_numbers_of_elements_count:
        element_number = elements_and_numbers_of_elements_count[key] - counter_decrease
        if element_number != 0:
            for i in range(element_number):
                output_sort_numbers.append(key)
                counter_decrease += 1
    return output_sort_numbers


print(counting_sort(input_numbers_to_sort))