# Task 1

class Graph:
    def __init__(self):
        # Initializes an empty dictionary to store vertices and their edges
        self.vertices = {}

    def add_vertex(self, vertex):
        # Adds a vertex to the graph if it doesn't already exist
        if vertex not in self.vertices:
            self.vertices[vertex] = {}

    def add_edge(self, source, destination, weight):
        # Adds an edge between two vertices with a given weight
        if source in self.vertices and destination in self.vertices:
            self.vertices[source][destination] = weight
            self.vertices[destination][source] = weight  # For undirected graph

    def get_neighbors(self, vertex):
        # Returns the neighbors of a given vertex along with the edge weights
        if vertex in self.vertices:
            return self.vertices[vertex]
        else:
            return {}


# Example usage:
graph = Graph()
graph.add_vertex('A')
graph.add_vertex('B')
graph.add_vertex('C')
graph.add_edge('A', 'B', 5)
graph.add_edge('B', 'C', 3)
graph.add_edge('A', 'C', 10)

# Output the graph structure
print(graph.vertices)
# Expected Output: {'A': {'B': 5, 'C': 10}, 'B': {'A': 5, 'C': 3}, 'C': {'A': 10, 'B': 3}}
