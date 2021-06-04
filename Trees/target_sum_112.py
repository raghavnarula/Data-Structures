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
        self.sum = 63
        self.value = 0
        self.val = False

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

    def target_sum (self,root):
        
        if root == None: # go up and find the sum..
            if self.value == self.sum:
                self.val = True
            return

        # print("root: ",root.dataval)
        self.value += root.dataval
        # print("value : ",self.value)

        self.target_sum(root.leftval)
        self.target_sum(root.rightval)

        self.value -= root.dataval

        # print("false")
        # self.val=Falseself.val=False


if __name__ == "__main__":
    root = Node(10)
    root.leftval = Node(8)
    root.rightval = Node(20)
    root.leftval.leftval = Node(5)
    root.leftval.rightval = Node(9)
    root.rightval.leftval = Node(15)
    root.rightval.rightval = Node(25)
    root.rightval.leftval.leftval = Node(13)
    root.rightval.leftval.rightval = Node(18)
    s = Tree()
    s.inorder(root)
    

if __name__ == "__main__":
    root = Node(10)
    root.leftval = Node(8)
    root.rightval = Node(20)
    root.leftval.leftval = Node(5)
    root.leftval.rightval = Node(9)
    root.rightval.leftval = Node(15)
    root.rightval.rightval = Node(25)
    root.rightval.leftval.leftval = Node(13)
    root.rightval.leftval.rightval = Node(18)
    s = Tree()
    s.inorder(root)
    
    s.printer()
    s.target_sum(root)

    print(s.val)

