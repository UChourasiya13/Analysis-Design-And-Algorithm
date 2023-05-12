# Binary search algorithm implementation in Python

def binary_search(arr, target):
    """
    Perform a binary search for the target integer in the given list of integers.

    Args:
    arr: List of integers to search in.
    target: Integer to search for.

    Returns:
    The index of the target integer in the list, if found. 
    Otherwise, returns -1.
    """
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            return mid

        elif arr[mid] < target:
            left = mid + 1

        else:
            right = mid - 1

    # Target integer not found in the list
    return -1


# Example usage
arr = [1, 3, 5, 7, 9]
target = 5

# Search for the target integer in the list using binary search
result = binary_search(arr, target)

if result != -1:
    print(f"Target {target} found at index {result}.")
else:
    print(f"Target {target} not found in the list.")
