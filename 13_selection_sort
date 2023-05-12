def selection_sort(arr):
    """
    Implementation of the selection sort algorithm for a list of integers.
    
    :param arr: A list of integers to be sorted.
    :return: The sorted list of integers.
    """
    n = len(arr)
    
    for i in range(n):
        # Find the index of the minimum element in the unsorted portion of the list.
        min_index = i
        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        
        # Swap the minimum element with the current element.
        arr[i], arr[min_index] = arr[min_index], arr[i]
    
    return arr


>>> my_list = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
>>> selection_sort(my_list)
[1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9]
