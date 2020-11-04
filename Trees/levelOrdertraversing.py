# two functions would be created that would be used for traversing in BFS.
# first is the print nodes at a given level.
# second is the print out the the levels in the tree...

class Node:
    def __init__(self,data):
        self.dataval = data
        self.leftval = None
        self.rightval = None


class Tree:
    def __init__(self,root):
        self.q = [root]
    def traversal(self,root):
        while (len(self.q)>0):
            print(self.q[0].dataval)
            node = self.q.pop(0)

            if node.leftval is not None:
                self.q.append(node.leftval)
            if node.rightval is not None:
                self.q.append(node.rightval )
            
#         # repeat this process till we get the queue to be empty

root = Node(1)
root.leftval = Node(2)
root.rightval = Node(3)
root.leftval.leftval = Node(4)
root.leftval.rightval =Node(5)
root.rightval.leftval = Node(8)
root.rightval.rightval = Node(8)

s = Tree(root)
s.traversal(root)