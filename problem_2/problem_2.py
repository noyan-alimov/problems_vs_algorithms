def rotated_array_search(input_list, number):
    """
    Find the index by searching in a rotated sorted array

    Args:
        input_list(array), number(int): Input array to search and the target
    Returns:
        int: Index or -1
    """
    if not isinstance(input_list, list):
        return -1

    if len(input_list) == 0:
        return -1

    start_index = 0
    end_index = len(input_list) - 1

    while start_index + 1 < end_index:
        mid_index = (start_index + end_index) // 2
        mid_value = input_list[mid_index]

        if mid_value == number:
            return mid_index

        if input_list[start_index] < mid_value < input_list[end_index]:
            if number > mid_value:
                start_index = mid_index
            else:
                end_index = mid_index

        elif mid_value > input_list[start_index] and mid_value > input_list[end_index]:
            if input_list[start_index] <= number < mid_value:
                end_index = mid_index
            else:
                start_index = mid_index

        elif mid_value < input_list[start_index] and mid_value < input_list[end_index]:
            if mid_value < number <= input_list[end_index]:
                start_index = mid_index
            else:
                end_index = mid_index

    if input_list[start_index] == number:
        return start_index
    elif input_list[end_index] == number:
        return end_index
    else:
        return -1

print(rotated_array_search([6, 7, 8, 1, 2, 3, 4], 8))



def linear_search(input_list, number):
    for index, element in enumerate(input_list):
        if element == number:
            return index
    return -1

def test_function(test_case):
    input_list = test_case[0]
    number = test_case[1]
    if linear_search(input_list, number) == rotated_array_search(input_list, number):
        print("Pass")
    else:
        print("Fail")

test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 6])
test_function(['hello', -1])  # expect to return -1 because input is not a list
test_function([[6, 7, 8, 1, 2, 3, 4], 8])
test_function([[], -1]) # expect to return -1 because input is an empty list
test_function([[6, 7, 8, 1, 2, 3, 4], 10]) # expect to return -1 because 10 is not in the list