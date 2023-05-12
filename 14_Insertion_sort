def insertion_sort(arr):
    """
    Sorts a list of integers using the insertion sort algorithm.

    Args:
        arr (list): A list of integers to be sorted.

    Returns:
        list: The sorted list of integers.
    """

    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

    return arr
