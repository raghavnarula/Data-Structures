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

    def bfs (self,root):
        # this if for the bfs traveral of the tree.
        q = []
        print("BFS: ",end=" ")
        # append in q  the cildren whever we encounter a node in tree.
        q.append(root)

        if len(q) <= 0:
            return
        
        while len(q) != 0:

            root = q[0]

            if root == "None":
                a = q.pop(0)
                print(a,end=" ")
                continue
            
            if root.rightval and root.leftval is not None:
                q.append(root.leftval)
                q.append(root.rightval)
            elif root.rightval is not None and root.leftval is None:
                q.append("None")
                q.append(root.rightval)
            elif root.leftval is not None and root.rightval is None:
                q.append(root.leftval)
                q.append("None")
            else:
                q.append("None")
                q.append("None")

            a = q.pop(0)
            print(a.dataval,end=" ")
        
        print()

    def dfs(self,root):
        
        if root == None:
            return

        print(root.dataval,end=" ")

        self.dfs(root.leftval)
        self.dfs(root.rightval)
    




if __name__ == "__main__":
    # root = Node(10)
    # root.leftval = Node(11)
    # root.rightval = Node(9)
    # root.leftval.leftval = Node(7)
    # root.rightval.leftval = Node(15)
    # root.rightval.rightval = Node(8)
    # root.leftval.rightval = Node(12)
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
    s.preorder(root)
    s.postorder(root)
    s.printer()

    s.bfs(root)

    s.dfs(root)
