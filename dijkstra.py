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

# Task 2

def dijkstra(graph, start_vertex):
    # Initialize distances and predecessors
    distances = {vertex: float('infinity') for vertex in graph.vertices}
    distances[start_vertex] = 0
    predecessors = {vertex: None for vertex in graph.vertices}
    
    # Initialize the set of visited vertices
    visited = set()
    
    # Initialize the list of vertices to explore
    vertices_to_explore = list(graph.vertices.keys())
    
    while vertices_to_explore:
        # Select the vertex with the smallest distance
        current_vertex = min(vertices_to_explore, key=lambda vertex: distances[vertex])
        vertices_to_explore.remove(current_vertex)

        if distances[current_vertex] == float('infinity'):
            break
        
        visited.add(current_vertex)
        
        for neighbor, weight in graph.get_neighbors(current_vertex).items():
            if neighbor not in visited:
                new_distance = distances[current_vertex] + weight
                if new_distance < distances[neighbor]:
                    distances[neighbor] = new_distance
                    predecessors[neighbor] = current_vertex

    return distances, predecessors

# Task 3 Test Cases

# Test Case 1 Simple Graph 

graph = Graph()
graph.add_vertex('A')
graph.add_vertex('B')
graph.add_vertex('C')
graph.add_vertex('D')
graph.add_edge('A', 'B', 1)
graph.add_edge('A', 'C', 4)
graph.add_edge('B', 'C', 2)
graph.add_edge('B', 'D', 5)
graph.add_edge('C', 'D', 1)

distances, predecessors = dijkstra(graph, 'A')
print("Test Case 1:")
print("Shortest path distances:", distances)
print("Shortest path predecessors:", predecessors)


# Test Case 2 Larger Graph

graph = Graph()
graph.add_vertex('A')
graph.add_vertex('B')
graph.add_vertex('C')
graph.add_vertex('D')
graph.add_vertex('E')
graph.add_vertex('F')
graph.add_edge('A', 'B', 2)
graph.add_edge('A', 'C', 1)
graph.add_edge('B', 'D', 5)
graph.add_edge('B', 'E', 2)
graph.add_edge('C', 'F', 8)
graph.add_edge('D', 'E', 3)
graph.add_edge('E', 'F', 1)

distances, predecessors = dijkstra(graph, 'A')
print("Test Case 2:")
print("Shortest path distances:", distances)
print("Shortest path predecessors:", predecessors)

# Test Case 3 Disconnected Graph

graph = Graph()
graph.add_vertex('A')
graph.add_vertex('B')
graph.add_vertex('C')
graph.add_vertex('D')
graph.add_vertex('E')
graph.add_edge('A', 'B', 3)
graph.add_edge('A', 'C', 5)
graph.add_edge('B', 'C', 1)
graph.add_edge('C', 'D', 2)

distances, predecessors = dijkstra(graph, 'A')
print("Test Case 3:")
print("Shortest path distances:", distances)
print("Shortest path predecessors:", predecessors)


