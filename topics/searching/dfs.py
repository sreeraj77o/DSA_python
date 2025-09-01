class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v):
        if u not in self.graph:
            self.graph[u] = []
        self.graph[u].append(v)

    def dfs(self, start, visited=None):
            """Depth-First Search"""
            if visited is None:
                visited = set()
            visited.add(start)
            print(start, end=" ")
            
            for neighbor in self.graph.get(start, []):
                if neighbor not in visited:
                    self.dfs(neighbor, visited)

g = Graph()
g.add_edge(0,1)
g.add_edge(0, 2)
g.add_edge(1, 2)
g.add_edge(2, 0)
g.add_edge(2, 3)
g.add_edge(3, 3)
g.dfs(2)