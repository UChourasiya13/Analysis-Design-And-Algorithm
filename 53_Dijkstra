import heapq

def dijkstra(graph, start, end):
    # Initialize distances dictionary with infinity values
    distances = {node: float('inf') for node in graph}
    # Set distance to starting node to 0
    distances[start] = 0
    # Initialize heap with starting node and its distance
    heap = [(0, start)]
    # Initialize path dictionary to keep track of the shortest path to each node
    path = {start: []}
    
    while heap:
        # Pop the node with the smallest distance from the heap
        (current_distance, current_node) = heapq.heappop(heap)
        
        # If the current node is the end node, return the path to it
        if current_node == end:
            return path[current_node] + [current_node]
        
        # Loop through the neighbors of the current node
        for neighbor, weight in graph[current_node].items():
            # Calculate the new distance to the neighbor
            distance = current_distance + weight
            # If the new distance is shorter than the current distance to the neighbor, update it
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                # Update the path to the neighbor
                path[neighbor] = path[current_node] + [current_node]
                # Push the neighbor and its new distance to the heap
                heapq.heappush(heap, (distance, neighbor))
    
    # If the end node is not reachable from the starting node, return None
    return None
