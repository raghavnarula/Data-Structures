class newNode:
    def __init__(self,data):
        self.data = data
        self.left = self.right = None
 
""" 
So the tree...
         4
        / \
        2  5
       / \
       1 3
 
is changed to...
     4
    / \
    5 2
      / \
      3 1
"""
def mirror(root):
    if root.right==None and root.left == None:
        return
    if root.right or root.left:
    # exchange
        root.right,root.left = root.left,root.right
    mirror(root.left)
    mirror(root.right)
    
 
 
def inOrder(node) :
 
    if (node == None):
        return
         
    inOrder(node.left)
    print(node.data, end = " ")
    inOrder(node.right)
 
# Driver code
if __name__ =="__main__":
 
    root = newNode(1)
    root.left = newNode(2)
    root.right = newNode(3)
    root.left.left = newNode(4)
    root.left.right = newNode(5)
    
    print("Inorder traversal of the constructed tree is")
    inOrder(root)
     
    mirror(root)
 
    print("\n Inorder traversal of the mirror tree is")
    inOrder(root)