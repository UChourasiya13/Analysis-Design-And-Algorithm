from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def dfs_util(self, u, v, visited, path):
        visited[u] = True
        path.append(u)
        if u == v:
            return path
        for i in self.graph[u]:
            if not visited[i]:
                res = self.dfs_util(i, v, visited, path)
                if res:
                    return res
        path.pop()
        return None

    def dfs(self, u, v):
        visited = {node: False for node in self.graph}
        path = []
        res = self.dfs_util(u, v, visited, path)
        if res:
            return res
        return "No path found between {} and {}".format(u, v)
