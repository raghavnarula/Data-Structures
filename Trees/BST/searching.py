# You are given a preorder traversal and now you want to insert in that
import insertion

class Node: 
  
    # Constructor to create a new node 
    def __init__(self, key): 
        self.dataval = key 
        self.leftval = None
        self.rightval = None
    
class Tree(insertion.Tree):
    def search(self,root,key): 
    # Base Cases: root is null or key is present at root 
        if root is None or root.dataval == key:
            if root is None:
                print("Not found")
            else:
                print(f"element found")
            return root 
    
        # Key is greater than root's key 
        if root.dataval < key: 
            return Tree.search(self,root.rightval,key) 
        # Key is smaller than root's key 
        return Tree.search(self,root.leftval,key) 

        

if __name__ == "__main__":
    tree = Tree()
    r = Node(50) 
    r = tree.insert(r, 30) 
    r = tree.insert(r, 20) 
    r = tree.insert(r, 40) 
    r = tree.insert(r, 70) 
    r = tree.insert(r, 60) 
    r = tree.insert(r, 80) 
    # tree.insert()
    tree.preorder(r)
    tree.printer()
    tree.search(r,1000)