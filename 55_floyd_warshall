# Function to find the shortest path between all pairs of nodes in a graph
# using the Floyd-Warshall algorithm
def floyd_warshall(graph):
    n = len(graph)
    # Initialize the distance matrix with the values of the graph
    dist = [[graph[i][j] for j in range(n)] for i in range(n)]
    # Loop over all nodes as intermediate points and update the distances
    for k in range(n):
        for i in range(n):
            for j in range(n):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
    return dist

# Example usage
graph = [[0, 5, float('inf'), 10],
         [float('inf'), 0, 3, float('inf')],
         [float('inf'), float('inf'), 0, 1],
         [float('inf'), float('inf'), float('inf'), 0]]
dist = floyd_warshall(graph)
print(dist)
