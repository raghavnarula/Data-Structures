## Two ways to implement graphs in python
## We are using the adjacenct matrix version
import sys
import numpy as np

class AdjNode:
    def __init__(self,data):
        self.vertex = data
        self.next = None


class Graph:
    def __init__(self,vertices):
        self.V = vertices 
        self.graph = np.zeros((self.V,self.V),dtype=np.uint8)
        self.list_vertex = []

    def vertex(self,number):
        AdjNode(number)
        self.list_vertex.append(number)

    def add_edge(self,start,end):
        if start in self.list_vertex and end in self.list_vertex:
            if self.graph[start-1][end-1] == 1:
                print('Edge already exists!')
            else:
                self.graph[start-1][end-1] = 1
                self.graph[end-1][start-1] = 1
        else:
            print('Vertex does not exist !')
            sys.exit()

    def graph_made(self):
        return self.graph

    def display(self):
        print(f'UnDirected Grpah ! {(self.V,self.V)}')
        for i in range(0,self.V):
            print("-------------------")
            for j in range(0,self.V):
                print(self.graph[i][j],end=" | ")
            print()

if __name__ == '__main__':  
    g = Graph(5)
    for i in range(1,6):
        g.vertex(i)
    
    g.add_edge(1,2)
    g.add_edge(1,3)
    g.add_edge(1,4)
    g.add_edge(2,3)
    g.add_edge(2,5)
    g.add_edge(3,5)
    g.add_edge(4,5)
    g.add_edge(5,4)

    g.display() 
