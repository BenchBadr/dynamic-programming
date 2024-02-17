import numpy as np

class Graph:
    def __init__(self, num_vertices):
        self.num_vertices = num_vertices
        self.adj_matrix = np.zeros((num_vertices, num_vertices))

    def add_edge(self, v1, v2, weight=1):
        self.adj_matrix[v1][v2] = weight
        self.adj_matrix[v2][v1] = weight  # If it's an undirected graph

    def remove_edge(self, v1, v2):
        self.adj_matrix[v1][v2] = 0
        self.adj_matrix[v2][v1] = 0  # If it's an undirected graph

    def __str__(self):
        return str(self.adj_matrix)
    
if __name__ == "__main__":
    num_vertices = 5
    graph = Graph(num_vertices)

    graph.add_edge(0, 1)
    graph.add_edge(0, 2)
    graph.add_edge(1, 3)
    graph.add_edge(2, 4)

    print("Graph Matrix Representation:")
    print(graph)