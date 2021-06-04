# leftval root rightval
# data leftval rightval
# leftval rightval root

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

    def same_tree (self,root1,root2):
        
        
        if root1==None and root2==None:
            return True

        # print("Checking:",root1.dataval,root2.dataval)

        if root1.dataval != root2.dataval:
            return False

        if root1!=None or root2!=None:
            return (self.same_tree(root1.leftval,root2.leftval) and self.same_tree(root1.rightval,root2.rightval))
        
        return 0

  

if __name__ == "__main__":
    root1 = Node(10);
    root2 = Node(10);

    root1.leftval = Node(7);
    root1.rightval = Node(15);
    root1.leftval.leftval = Node(4);
    # root1.leftval.rightval = Node(9);
    root1.rightval.rightval = Node(20);
  
    root2.leftval = Node(7);
    root2.rightval = Node(15);
    # root2.leftval.leftval = Node(4);
    root2.leftval.rightval = Node(9);
    root2.rightval.rightval = Node(20);
    s = Tree()

    print(s.same_tree(root1,root2))

