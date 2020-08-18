def mergesort(items):

    if len(items) <= 1:
        return items
    
    mid = len(items) // 2
    left = items[:mid]
    right = items[mid:]
    
    left = mergesort(left)
    right = mergesort(right)
    
    return merge(left, right)
    
def merge(left, right):
    
    merged = []
    left_index = 0
    right_index = 0
    
    while left_index < len(left) and right_index < len(right):
        if left[left_index] > right[right_index]:
            merged.append(right[right_index])
            right_index += 1
        else:
            merged.append(left[left_index])
            left_index += 1

    merged += left[left_index:]
    merged += right[right_index:]
        
    return merged



def rearrange_digits(input_list):
    """
    Rearrange Array Elements so as to form two number such that their sum is maximum.

    Args:
       input_list(list): Input List
    Returns:
       (int),(int): Two maximum sums
    """
    if not isinstance(input_list, list):
        return None

    if len(input_list) == 0:
        return []

    sorted_list = mergesort(input_list)
    
    n = len(sorted_list)

    output1 = list()
    output2 = list()

    for i in range(n, 0, -1):
        num = sorted_list.pop()
        if i % 2 == 0:
            output1.append(num)
        else:
            output2.append(num)
    
    result1 = ''.join(str(n) for n in output1)
    result2 = ''.join(str(n) for n in output2)

    return [int(result1), int(result2)]



print(rearrange_digits([4, 6, 2, 5, 9, 8])) # expect to return [964, 852]
print(rearrange_digits(1)) # expect to return None because of invalid input
print(rearrange_digits([])) # expect to return an empty array due to input being an empty array
print(rearrange_digits([1, 2, 3, 4, 5])) # expect to return [42, 531]

