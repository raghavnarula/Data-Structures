# You are given a preorder traversal and now you want to insert in that
import sys
import traversals
class Node: 
  
    # Constructor to create a new node 
    def __init__(self, key): 
        self.dataval = key 
        self.leftval = None
        self.rightval = None
    
class Tree(traversals.Tree):
    def insert(self,root, key):
        if root is None: 
            print("here the insertion takes place")
            return Node(key) # here the insertion takes place .
        else: 
            if root.dataval == key: 
                print("This is the thing")
                return root 
            elif root.dataval < key: 
                root.rightval = Tree.insert(self,root.rightval, key) 
            else: 
                root.leftval = Tree.insert(self,root.leftval, key)
        # print("I am doing something")
        return root 
    
if __name__ == "__main__":
    tree = Tree()
    r = Node(50) 
    r = tree.insert(r, 30)
    r = tree.insert(r, 20) 
    r = tree.insert(r, 40) 
    r = tree.insert(r, 70) 
    r = tree.insert(r, 60) 
    r = tree.insert(r, 80) 
    tree.insert(r,100)
    tree.preorder(r)
    tree.printer()