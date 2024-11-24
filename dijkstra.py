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


# Task 4

# *Time and Space Complexity Analysis*

# ~Time Complexity~ 

# Initialization:
# Initializing the distances dictionary and the predecessors dictionary takes 𝑂(𝑉) time, where 𝑉 is the number of vertices.

# Finding Minimum Distance Vertex:
# Each time we need to find the vertex with the smallest distance from the list of vertices to explore, it takes 𝑂(𝑉) time. 
# Since we do this for each vertex, the total time for these operations is 𝑂(𝑉^2).

# Edge Relaxation:
# For each vertex, we look at all its adjacent vertices (edges). 
# This operation is performed for each edge once, resulting in a total time of 𝑂(𝐸), where 𝐸 is the number of edges.
# Combining these, the overall time complexity is: 𝑂(𝑉^2+𝐸)


# ~Space Complexity~

# Distances Dictionary:
# Requires 𝑂(𝑉) space to store the shortest distance for each vertex.

# Predecessors Dictionary:
# Requires 𝑂(𝑉) space to store the predecessor for each vertex.

# Graph Representation (Adjacency List):
# Requires 𝑂(𝑉+𝐸) space to store the graph.
# Combining these, the overall space complexity is:𝑂(𝑉+𝐸)


# ~Insights into Efficiency and Optimization~

# Efficiency:
# This implementation is simple but less efficient, especially for dense graphs with a large number of vertices. 
# The 𝑂(𝑉2+𝐸) time complexity can be prohibitive for large graphs.

# Optimization Opportunity:
# The primary inefficiency lies in the time complexity of finding the minimum distance vertex. 
# This operation can be optimized by using a more efficient data structure such as a priority queue.

# ~Potential Optimization~
# Using a priority queue (like heapq) can significantly improve the efficiency of Dijkstra's algorithm by reducing the time complexity to 𝑂((𝑉+𝐸)log𝑉). 
# This is because finding and updating the minimum distance vertex can be done in 𝑂(log⁡𝑉) time using a priority queue.