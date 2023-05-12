# Import heapq for implementing priority queue
import heapq

def prim(graph):
    """
    :param graph: adjacency list representation of the graph
    :return: list of edges in the minimum spanning tree
    """
    # Initialize the set of visited vertices and the priority queue
    visited = set()
    queue = [(0, None, 0)]
    # List to store the edges in the minimum spanning tree
    mst = []

    while queue:
        # Pop the vertex with the smallest weight from the priority queue
        weight, u, v = heapq.heappop(queue)
        # If the vertex has already been visited, continue
        if v in visited:
            continue
        # Add the vertex to the visited set
        visited.add(v)
        # Add the edge to the minimum spanning tree
        if u is not None:
            mst.append((u, v, weight))
        # Add the neighbors of the current vertex to the priority queue
        for neighbor, weight in graph[v]:
            if neighbor not in visited:
                heapq.heappush(queue, (weight, v, neighbor))

    return mst
