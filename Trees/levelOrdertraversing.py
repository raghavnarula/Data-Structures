# two functions would be created that would be used for traversing in BFS.
# Using queue

# insert the root append the left child and then the right child of the root.

class Node:
    def __init__(self,data):
        self.dataval = data
        self.left = None
        self.right = None


def printLevelOrder(root):
    if root is None:
        return
    
    queue = []

    queue.append(root)

    while (len(queue) > 0):
        print(queue[0].dataval)

        node = queue.pop(0)

        #Enqueue left child
        if node.left is not None:
            queue.append(node.left)
 
        # Enqueue right child
        if node.right is not None:
            queue.append(node.right)

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

printLevelOrder(root)