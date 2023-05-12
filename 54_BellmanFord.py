from typing import List, Tuple

# Define a class to represent the graph
class Graph:
    def __init__(self, num_vertices: int):
        self.num_vertices = num_vertices
        self.edges = []

    def add_edge(self, src: int, dest: int, weight: int):
        self.edges.append((src, dest, weight))

    def bellman_ford(self, src: int, dest: int) -> Tuple[List[int], List[int]]:
        # Step 1: Initialize distances from src to all other vertices as infinite
        # and distance to src itself as 0.
        dist = [float('inf')] * self.num_vertices
        dist[src] = 0

        # Step 2: Relax all edges |V| - 1 times. A simple shortest path
        # from src to any other vertex can have at-most |V| - 1 edges
        for _ in range(self.num_vertices - 1):
            for src_vertex, dest_vertex, weight in self.edges:
                if dist[src_vertex] != float('inf') and dist[src_vertex] + weight < dist[dest_vertex]:
                    dist[dest_vertex] = dist[src_vertex] + weight

        # Step 3: Check for negative-weight cycles. The above step
        # guarantees shortest distances if graph doesn't contain negative weight cycle.
        # If we get a shorter path, then there is a cycle.
        for src_vertex, dest_vertex, weight in self.edges:
            if dist[src_vertex] != float('inf') and dist[src_vertex] + weight < dist[dest_vertex]:
                raise ValueError("Graph contains negative weight cycle")

        return dist, None

# Example usage
g = Graph(5)
g.add_edge(0, 1, -1)
g.add_edge(0, 2, 4)
g.add_edge(1, 2, 3)
g.add_edge(1, 3, 2)
g.add_edge(1, 4, 2)
g.add_edge(3, 2, 5)
g.add_edge(3, 1, 1)
g.add_edge(4, 3, -3)

src, dest = 0, 2
dist, _ = g.bellman_ford(src, dest)
print(f"Shortest path from {src} to {dest}: {dist[dest]}")
