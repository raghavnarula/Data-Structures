class Node:
    def __init__(self,data):
        self.dataval = data
        self.leftval = None
        self.rightval = None
    
class Tree:
    def __init__(self,root):
        self.q = [root]
        self.q2 = []
    def insert(self,root,node):
        # new_node = Node(data)
        # traverse like BFS
        while(1):
            if self.q[0].leftval is None:
                # then insert the value 
                self.q[0].leftval  = node
                break
            elif self.q[0].rightval is None:
                self.q[0].rightval = node
                break
            else:
                self.q.append(self.q[0].leftval)
                self.q.append(self.q[0].rightval)
            
            del self.q[0]
    
    def inorder(self,root):
        if root is None:
            return
        else:
            Tree.inorder(self,root.leftval)
            self.q2.append(root.dataval)
            Tree.inorder(self,root.rightval)
    
    def printer(self):
        print(self.q2)


if __name__ == '__main__':
    root = Node(10)
    root.leftval = Node(11)
    root.rightval = Node(9)
    root.leftval.leftval = Node(7)
    root.rightval.leftval = Node(15)
    root.rightval.rightval = Node(8)

    s = Tree(root)
    s.insert(root,Node(12))

    s.inorder(root)
    s.printer()


        



            
