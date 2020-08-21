# first creating 
class Node:
    def __init__(self,dataval=None):
        self.dataval = dataval
        self.nextval = None
    
class SlinkedList():
    def __init__(self):
        self.headval = None
    
    def print_list(self):
        printval = self.headval

        while printval is not None:
            print(printval.dataval)
            printval = printval.nextval
        
list = SlinkedList()
list.headval = Node("Mon")
e2 = Node("Tue")
e3 = Node("Wed")

# Link first Node to second node
list.headval.nextval = e2

# Link second Node to third node
e2.nextval = e3

list.print_list()