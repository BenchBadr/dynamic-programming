import numpy as np
from queue import Queue
from stack import Stack

class Graph:
    def __init__(self):
        self.adj_matrix = np.zeros((1,1), dtype=np.int32)

    def add_edge(self, v1, v2):
        v1, v2 = (ord(v.lower())  - ord('a') for v in (v1, v2))
        order = self.adj_matrix.shape[0]
        print(max(v1, v2), order)9
        if max(v1, v2) > order-1:
            self.adj_matrix = np.column_stack((self.adj_matrix, np.zeros((order,1), dtype=np.int32)))
            self.adj_matrix = np.vstack((self.adj_matrix, np.zeros((1,order+1), dtype=np.int32)))
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
    
    def get_neigh(self, v):
        v = ord(v.lower()) - ord('a')
        return [chr(ord('a')+index) for index, node in enumerate(self.adj_matrix[v]) if node==1]

    def bfs(self):
        s = Queue()
        x = 'a'
        visited = [x]
        s.enqueue(x)
        out = []

        while not s.is_empty():
            x = s.dequeue()
            out.append(x.upper())
            neigh = self.get_neigh(x)
            for n in neigh:
                if n not in visited:
                    visited.append(n)
                    s.enqueue(n)

        return out
    
    def dfs(self):
        s = Stack()
        x = 'a'
        visited = [x]
        s.push(x)
        out = []

        while not s.is_empty():
            x = s.pop()
            out.append(x.upper())
            neigh = self.get_neigh(x)
            for n in neigh[::-1]:
                if n not in visited:
                    visited.append(n)
                    s.push(n)

        return out       

    
if __name__ == "__main__":
    graph = Graph()

    graph.add_edge('A', 'B')
    graph.add_edge('B', 'F')
    graph.add_edge('A', 'C')
    graph.add_edge('C','D')
    graph.add_edge('C','E')


    print(graph)

    print(graph.get_degree('a'))
    print(graph.get_degree('b'))
    print(graph.edge_numbers())
    print(graph.get_neigh('A'))

    print('-'*20)

    print(graph.bfs())
    print(graph.dfs())