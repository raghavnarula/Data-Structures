class Node:
    def __init__(self,data):
        self.dataval = data
        self.leftval = None
        self.rightval = None


class Tree:
    def printer_left(self,headval,side):  # prints the left most side of the linked list
        # root is the head
        if side == 'left':
            while (headval is not None):
                print(headval.dataval)
                headval = headval.leftval
        else:
            while (headval is not None):
                print(headval.dataval)
                headval = headval.rightval


root = Node(10)
child1_left = Node(20)
child1_right = Node(30)
root.leftval = child1_left
root.rightval = child1_right
child1_left.leftval = Node(40)

'''
        10
       /  \
      20   30
    /   \
   40   50
'''
#  I am seeing a pattern here that the left most side and the right most side can be printed as singly linked list.

T1 = Tree()
T1.printer_left(root,'right')



