import heapq
import math

def dijkstra(graph, start, end):
    """
    Finds the shortest path between the start and end vertices in the given graph using Dijkstra's algorithm.
    
    Parameters:
    - graph: a dictionary representing the graph where each key is a vertex and the corresponding value is a dictionary of adjacent vertices and edge weights
    - start: the starting vertex
    - end: the ending vertex
    
    Returns:
    - A tuple containing two items:
      1. The minimum distance between the start and end vertices
      2. The shortest path between the start and end vertices as a list of vertices
    """
    # Create a dictionary to keep track of the minimum distances to each vertex
    distances = {vertex: math.inf for vertex in graph}
    distances[start] = 0
    
    # Create a dictionary to keep track of the previous vertex in the shortest path to each vertex
    previous_vertices = {vertex: None for vertex in graph}
    
    # Create a priority queue to hold vertices to be visited, ordered by their distance from the start vertex
    priority_queue = [(0, start)]
    
    # Loop while there are vertices in the priority queue
    while priority_queue:
        # Get the vertex with the smallest distance from the start vertex
        current_distance, current_vertex = heapq.heappop(priority_queue)
        
        # If we have already visited the current vertex, continue to the next vertex in the priority queue
        if current_distance > distances[current_vertex]:
            continue
        
        # Loop over the adjacent vertices to the current vertex
        for neighbor, weight in graph[current_vertex].items():
            # Calculate the distance to the neighbor vertex
            distance = current_distance + weight
            
            # If the new distance to the neighbor is less than the current distance, update the distance and previous vertex
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous_vertices[neighbor] = current_vertex
                heapq.heappush(priority_queue, (distance, neighbor))
    
    # Build the shortest path as a list of vertices by following the previous vertex pointers from the end vertex to the start vertex
    shortest_path = []
    current_vertex = end
    while current_vertex is not None:
        shortest_path.append(current_vertex)
        current_vertex = previous_vertices[current_vertex]
    shortest_path.reverse()
    
    # Return the minimum distance and shortest path as a tuple
    return distances[end], shortest_path
