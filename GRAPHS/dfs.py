from bfs import Graph
import numpy as np
import sys
class Graph(Graph):
    def __init__(self,vertices):
        visited_nodes = []
        self.V = vertices
        self.graph = np.zeros((self.V,self.V),dtype=np.uint8)
        self.list_vertex = []
        self.queue = []
        self.dfs_list = []

    
    def dfs(self,head_vertex):
        pass
