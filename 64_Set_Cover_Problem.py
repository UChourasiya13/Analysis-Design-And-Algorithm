import sys

# Define a function to solve the Set Cover Problem
def set_cover(universe, subsets):
    # Create a list to keep track of the elements not yet covered
    elements = set(e for s in subsets for e in s)
    # Create an empty list to store the chosen subsets
    chosen_subsets = []
    # Loop until all elements are covered
    while elements:
        # Choose the subset that covers the most uncovered elements
        best_subset = max(subsets, key=lambda s: len(s & elements))
        # Add the chosen subset to the list of chosen subsets
        chosen_subsets.append(best_subset)
        # Remove the covered elements from the list of uncovered elements
        elements -= best_subset
    # Return the list of chosen subsets
    return chosen_subsets


# Example usage
universe = set(range(1, 11))
subsets = [set([1, 2, 3, 8, 9, 10]), set([1, 2, 3, 4, 5]), set([4, 5, 7]), set([5, 6, 7]), set([6, 7, 8, 9, 10])]
chosen_subsets = set_cover(universe, subsets)
print(chosen_subsets)
