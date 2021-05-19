from graphs_representations import Graph
import numpy as np
import sys
class Graph(Graph):
    def __init__(self,vertices):
        visited_nodes = []
        self.V = vertices
        self.graph = np.zeros((self.V,self.V),dtype=np.uint8)
        self.list_vertex = []
        self.queue = []
        self.bfs_list = []
        
    # We already have a graph 
    def bfs(self,head_vertex):
        print("Final : ",self.bfs_list,"Queue : ",self.queue)        
        if head_vertex in self.queue or head_vertex in self.bfs_list:
            pass
        else:
            self.queue.append(head_vertex)
        for i in range(self.V):
            # print(i,end=" ")
            if self.graph[head_vertex-1][i] == 1:
                # put (i+1) into the set queue.
                # before appending see if the queue already has the element in it
                if i+1 in self.bfs_list or i+1 in self.queue:
                    pass
                else:
                    print("I am appending",i+1)
                    # if i+2 in self.
                    self.queue.append(i+1)

        
        vertex_ins = self.queue.pop(0)
        self.bfs_list.append(vertex_ins)
        if len(self.bfs_list) == self.V:
            print("Final",self.bfs_list)
            return 
            sys.exit()
        return self.bfs(self.queue[0])

        # print(i)
if __name__ == "__main__":
    vertices = 4
    g = Graph(vertices)
    for i in range(1,vertices+1):
        g.vertex(i)
    g.add_edge(1,2)
    g.add_edge(1,3)
    g.add_edge(2,3)
    g.add_edge(3,4)
    g.add_edge(4,4)
    g.display()
    g.bfs(3)

