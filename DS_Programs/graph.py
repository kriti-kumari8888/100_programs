from collections import defaultdict, deque

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
    
    def add_edge(self, u, v):
        """Add an edge to the graph."""
        self.graph[u].append(v)
    
    def bfs(self, start):
        """Perform Breadth First Search starting from given vertex."""
        visited = set()
        queue = deque([start])
        visited.add(start)
        
        while queue:
            vertex = queue.popleft()
            print(vertex, end=" ")
            
            for neighbor in self.graph[vertex]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
    
    def dfs(self, start):
        """Perform Depth First Search starting from given vertex."""
        visited = set()
        self._dfs_recursive(start, visited)
    
    def _dfs_recursive(self, vertex, visited):
        visited.add(vertex)
        print(vertex, end=" ")
        
        for neighbor in self.graph[vertex]:
            if neighbor not in visited:
                self._dfs_recursive(neighbor, visited)

def main():
    # Example usage
    g = Graph()
    
    # Add edges to the graph
    edges = [(0, 1), (0, 2), (1, 2), (2, 0), (2, 3), (3, 3)]
    for u, v in edges:
        g.add_edge(u, v)
    
    print("Breadth First Traversal (starting from vertex 2):")
    g.bfs(2)
    
    print("\n\nDepth First Traversal (starting from vertex 2):")
    g.dfs(2)
    print()

if __name__ == "__main__":
    main()