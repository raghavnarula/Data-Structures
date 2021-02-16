# keep moving to the left node until we find null

class Node: 
  
    # Constructor to create a new node 
    def __init__(self, key): 
        self.data = key 
        self.leftval = None
        self.rightval = None

def minValue(node): 
    current = node 

    # loop down to find the lefmost leaf 
    while(current.leftval is not None): 
        current = current.leftval 

    return current.data 

root = Node(10)
root.leftval = Node(8)
root.rightval = Node(14)
root.leftval.leftval = Node(5)
root.rightval.leftval = Node(13)
root.rightval.rightval = Node(16)
root.leftval.rightval = Node(9)

print(minValue(root))