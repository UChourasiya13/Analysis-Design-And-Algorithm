from queue import PriorityQueue
from itertools import permutations

def tsp(graph):
    # Initialize variables
    n = len(graph)
    visited = set()
    min_path = float("inf")
    min_path_order = None

    # Create a priority queue for storing nodes to visit
    pq = PriorityQueue()

    # Initialize with starting node and path cost 0
    pq.put((0, 0, [0]))

    # Loop until priority queue is empty
    while not pq.empty():
        # Get node with lowest lower bound
        _, cost, path = pq.get()

        # If all nodes have been visited, update min_path and min_path_order
        if len(path) == n:
            if cost < min_path:
                min_path = cost
                min_path_order = path
        else:
            # Generate children nodes by adding unvisited nodes to path
            for i in range(n):
                if i not in visited:
                    new_path = path + [i]
                    new_cost = cost + graph[path[-1]][i]

                    # Calculate lower bound of child node
                    lb = new_cost
                    for j in range(n):
                        if j not in visited and j != i:
                            lb += min(graph[j])

                    # Add child node to priority queue
                    pq.put((lb, new_cost, new_path))

        # Mark current node as visited
        visited.add(path[-1])

    return min_path, min_path_order

# Example usage
graph = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]
print(tsp(graph))
