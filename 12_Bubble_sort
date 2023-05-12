def bubble_sort(nums):
    """
    Sorts a list of integers in ascending order using the bubble sort algorithm.

    Args:
        nums: A list of integers to be sorted.

    Returns:
        The sorted list of integers.
    """
    # get the length of the list
    n = len(nums)

    # perform n iterations of bubble sort
    for i in range(n):
        # keep track of whether any swaps were made during this iteration
        swapped = False

        # compare each adjacent pair of elements in the list
        for j in range(n - i - 1):
            # if the current element is greater than the next element, swap them
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
                swapped = True

        # if no swaps were made during this iteration, the list is already sorted
        if not swapped:
            break

    return nums
# define an unsorted list of integers
nums = [5, 3, 8, 4, 2]

# sort the list using bubble sort
sorted_nums = bubble_sort(nums)

# print the sorted list
print(sorted_nums)

[2, 3, 4, 5, 8]
