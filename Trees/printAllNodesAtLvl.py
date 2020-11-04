'''
We want to print all the nodes at the given level..
'''

'''
                        1 
                    2       3
                 4    5    8
'''


class Node:
    def __init__(self,data):
        self.dataval = data
        self.leftval = None
        self.rightval = None
    
def printAtk(root,k):
    # suppose we are printing at level 1(topmost)
    if root is None:
        return 
    if k <= 0:
        #we are reaching the end of the state
        print(root.dataval)

    else:
        printAtk(root.leftval,k-1)
        printAtk(root.rightval,k-1)
        
root = Node(1)
root.leftval = Node(2)
root.rightval = Node(3)
root.leftval.leftval = Node(4)
root.leftval.rightval =Node(5)
root.rightval.leftval = Node(8)

printAtk(root,2)
