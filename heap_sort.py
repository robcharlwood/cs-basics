def _build_max_heap(nums):
    i = len(nums) / 2 - 1
    i = int(math.floor(i))
    while i >= 0:
        _heapify(nums, i, len(nums))
        i -= 1


def _swap(nums, first_index, last_index):
    tmp = nums[first_index]
    nums[first_index] = nums[last_index]
    nums[last_index] = tmp


def _heapify(heap, i, max_value):
    while i < max_value:
        index = i
        left_child = int(2 * i + 1)
        right_child = int(left_child + 1)

        if left_child < max_value and heap[left_child] > heap[index]:
            index = left_child

        if right_child < max_value and heap[right_child] > heap[index]:
            index = right_child

        if index == i:
            return

        _swap(heap, i, index)
        i = index


def heap_sort(nums):
    """
    Heap sort is O(n log n)
    Space complexity O(1)
    """
    _build_max_heap(nums)
    last_element = len(nums) - 1
    while last_element > 0:
        _swap(nums, 0, last_element)
        _heapify(nums, 0, last_element)
        last_element -= 1
    return nums
