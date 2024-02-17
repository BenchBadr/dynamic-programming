import numpy as np

class Graph:
    def __init__(self, num_vertices):
        self.num_vertices = num_vertices
        self.adj_matrix = np.zeros((num_vertices, num_vertices), dtype=np.int32)

    def add_edge(self, v1, v2):
        v1, v2 = (ord(v.lower())  - ord('a') for v in (v1, v2))
        print(v1, v2)
        self.adj_matrix[v1][v2] = 1
        self.adj_matrix[v2][v1] = 1

    def remove_edge(self, v1, v2):
        self.adj_matrix[v1][v2] = 0
        self.adj_matrix[v2][v1] = 0

    def __str__(self):
        return str(self.adj_matrix)
    
    def get_degree(self, v):
        v = ord(v.lower()) - ord('a')
        return sum(self.adj_matrix[v])
    
    def edge_numbers(self):
        return np.sum(self.adj_matrix)//2
    
if __name__ == "__main__":
    graph = Graph(5)

    graph.add_edge('A', 'B')
    graph.add_edge('A', 'C')


    print(graph)

    print(graph.get_degree('a'))
    print(graph.get_degree('b'))
    print(graph.edge_numbers())