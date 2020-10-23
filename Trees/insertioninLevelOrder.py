class Node:
    def __init__(self,data):
        self.dataval = data
        self.leftval = None
        self.rightval = None
    
class Tree:
    def __init__(self):
        pass
    def insert(self,root,data):
        new_node = Node(data)
        traverse = root
        while(traverse.leftval is not None or traverse.rightval is not None):
            if traverse.leftval is None:
                traverse.leftval = new_node
                break
            elif traverse.rightval is None:
                traverse.rightval = new_node
                break
            # now we need to move forward also if both conditions are checked

            # check at left child position first and then the right child posiition


            
