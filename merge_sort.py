def merge(lhalf, rhalf, numbers):
    index = 0

    while len(lhalf) > 0 and len(rhalf) > 0:
        if rhalf[0] < lhalf[0]:
            numbers[index] = rhalf.pop(0)
        else:
            numbers[index] = lhalf.pop(0)
        index += 1

    while len(lhalf) > 0:
        numbers[index] = lhalf.pop(0)
        index += 1

    while len(rhalf) > 0:
        numbers[index] = rhalf.pop(0)
        index += 1
    return numbers


def merge_sort(numbers):
    """
    Merge sort method
    This is an O (n log n) algorithm
    """
    if len(numbers) <= 1:
        return numbers
    half = len(numbers) / 2
    lhalf = merge_sort(numbers[:half])
    rhalf = merge_sort(numbers[half:])
    return merge(lhalf, rhalf, numbers)
