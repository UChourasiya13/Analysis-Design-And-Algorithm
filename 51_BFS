from collections import deque

# define a function to perform BFS
def bfs(graph, start, goal):
    # create a queue for BFS
    queue = deque()
    # enqueue the starting node and mark it as visited
    queue.append((start, [start]))
    visited = set([start])
    
    # loop until the queue is empty
    while queue:
        # dequeue the next node from the queue
        node, path = queue.popleft()
        # if we have found the goal node, return the path to it
        if node == goal:
            return path
        # otherwise, add all unvisited neighbors to the queue
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, path + [neighbor]))
    
    # if we have explored the entire graph and haven't found the goal node, there is no path
    return None
