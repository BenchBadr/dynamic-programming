import numpy as np
from queue import Queue
from stack import Stack

class Graph:
    def __init__(self):
        self.adj_matrix = [[0]]

    def add_edge(self, v1, v2, d = 1):
        order = len(self.adj_matrix)
        if max(v1, v2) > order-1:
            self.adj_matrix = [n+[0]*(max(v1,v2)-order+1) for n in self.adj_matrix]+[[0]*(max(v1,v2)+1) for i in range(max(v1,v2))]
        self.adj_matrix[v1][v2] = d
        # matrix is not symmetrical (oriented)
        #self.adj_matrix[v2][v1] = d

    def remove_edge(self, v1, v2):
        self.adj_matrix[v1][v2] = 0
        self.adj_matrix[v2][v1] = 0

    def __str__(self):
        return str(self.adj_matrix)
    
    def get_degree(self, v):
        return sum([int(n!=0) for n in self.adj_matrix[v]])
    
    def edge_numbers(self):
        return sum([sum(n) for n in self.adj_matrix])//2
    
    def get_neigh(self, v):
        return [index for index, node in enumerate(self.adj_matrix[v]) if node!=0]

    def bfs(self):
        s = Queue()
        x = 0
        visited = [x]
        s.enqueue(x)
        out = []

        while not s.is_empty():
            x = s.dequeue()
            out.append(x)
            neigh = self.get_neigh(x)
            for n in neigh:
                if n not in visited:
                    visited.append(n)
                    s.enqueue(n)

        return out
    
    def dfs(self):
        s = Stack()
        x = 0
        visited = [x]
        s.push(x)
        out = []

        while not s.is_empty():
            x = s.pop()
            out.append(x)
            neigh = self.get_neigh(x)
            for n in neigh[::-1]:
                if n not in visited:
                    visited.append(n)
                    s.push(n)

        return out

    
if __name__ == "__main__":
    graph = Graph()

    graph.add_edge(0,1)
    print(graph.bfs())
    # graph.add_edge('B', 'F')
    # graph.add_edge('A', 'C')
    # graph.add_edge('C','D')
    # graph.add_edge('C','E')


    # print(graph)

    # print(graph.get_degree('a'))
    # print(graph.get_degree('b'))
    # print(graph.edge_numbers())
    # print(graph.get_neigh('A'))

    # print('-'*20)

    # print(graph.bfs())
    # print(graph.dfs())
    # print(graph)