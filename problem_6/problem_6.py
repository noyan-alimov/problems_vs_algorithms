def get_min_max(ints):
    """
    Return a tuple(min, max) out of list of unsorted integers.

    Args:
        ints(list): list of integers containing one or more integers
    """
    if not isinstance(ints, list):
        return None

    if len(ints) == 0:
        return None

    min_num = ints[0]
    max_num = ints[0]

    for n in ints:
        if n < min_num:
            min_num = n

        if n > max_num:
            max_num = n

    return (min_num, max_num)

print(get_min_max([1, 3, 8, 7, 2, 4])) # expect (1, 8)
print(get_min_max([])) # expect None
print(get_min_max(1)) # expect None