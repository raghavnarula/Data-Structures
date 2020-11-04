# left root right
# data left right
# left right root

class Node:
    def __init__(self,data):
        self.dataval = data
        self.leftval = None
        self.rightval = None

class Tree:
    def __init__(self):
        self.q = []
        self.q2 = []
        self.q3 = []

    def inorder(self,root):
        if root is None:
            return 
        Tree.inorder(self,root.leftval)
        self.q.append(root.dataval)
        Tree.inorder(self,root.rightval)
    
    def printer(self):
        print("Inorder",self.q)
        print("Preorder",self.q2)
        print("Postorder",self.q3)

    def preorder(self,root):
        if root is None:
            return 
        self.q2.append(root.dataval)
        Tree.preorder(self,root.leftval)
        Tree.preorder(self,root.rightval)

    def postorder(self,root):
        if root is None:
            return 
        Tree.postorder(self,root.leftval)
        Tree.postorder(self,root.rightval)
        self.q3.append(root.dataval)


if __name__ == "__main__":
    root = Node(10)
    root.leftval = Node(11)
    root.rightval = Node(9)
    root.leftval.leftval = Node(7)
    root.rightval.leftval = Node(15)
    root.rightval.rightval = Node(8)
    root.leftval.rightval = Node(12)
    s = Tree()
    s.inorder(root)
    s.preorder(root)
    s.postorder(root)
    s.printer()
