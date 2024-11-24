# Task 2

class Graph:
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex):
        if vertex not in self.vertices:
            self.vertices[vertex] = {}

    def add_edge(self, source, destination, weight):
        if source in self.vertices and destination in self.vertices:
            self.vertices[source][destination] = weight
            self.vertices[destination][source] = weight  # For undirected graph

    def get_neighbors(self, vertex):
        if vertex in self.vertices:
            return self.vertices[vertex]
        else:
            return {}

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

# Example usage:
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

print("Shortest path distances:", distances)
print("Shortest path predecessors:", predecessors)
