def quick_sort(arr):
    """
    This function implements the Quick Sort algorithm for a list of integers.

    Parameters:
    arr (list): A list of integers to be sorted.

    Returns:
    list: The sorted list of integers.
    """
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return quick_sort(left) + middle + quick_sort(right)
