# Implementing linear search algorithm to find an element in a list of integers

def linear_search(arr, x):
    """
    This function takes in a list of integers and a target integer as arguments.
    It returns the index of the target integer in the list if it is present, 
    otherwise returns -1.
    """
    n = len(arr)
    for i in range(n):
        if arr[i] == x:
            return i
    return -1

# Example usage
arr = [5, 2, 4, 7, 9, 1]
x = 7
result = linear_search(arr, x)
if result == -1:
    print(f"{x} is not present in the list")
else:
    print(f"{x} is present at index {result}")
