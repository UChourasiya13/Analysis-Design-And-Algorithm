def knapsack_greedy(weights, values, capacity):
    # Calculate the value-to-weight ratio for each item
    ratios = [v/w for v, w in zip(values, weights)]

    # Sort the items in descending order of value-to-weight ratio
    sorted_items = sorted(zip(ratios, weights, values), reverse=True)

    # Initialize variables for tracking the current weight and value of the knapsack
    current_weight = 0
    current_value = 0

    # Loop through the sorted items and add as many as possible to the knapsack
    for ratio, weight, value in sorted_items:
        if current_weight + weight <= capacity:
            current_weight += weight
            current_value += value
        else:
            # Add a fractional amount of the item to fill the knapsack to capacity
            remaining_capacity = capacity - current_weight
            current_weight += remaining_capacity
            current_value += remaining_capacity * ratio
            break

    # Return the total value of the items in the knapsack
    return current_value
