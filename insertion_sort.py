def insertion_sort(numbers):
    """
    At worst this is an O(n2) algorithm
    At best this is an O(n) algorithm
    """
    for index in xrange(1, len(numbers)):
        current_num = numbers[index]
        current_pos = index
        while current_pos > 0 and numbers[current_pos - 1] > current_num:
            numbers[current_pos] = numbers[current_pos - 1]
            current_pos = current_pos - 1
        numbers[current_pos] = current_num
    return numbers
