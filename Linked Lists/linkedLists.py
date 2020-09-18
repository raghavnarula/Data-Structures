# We are creating a simple linked lists in python

class Node: # creating a node for the linked list 
    def __init__(self,dataval=None): # data to be inserted
        self.dataval = dataval
        self.nextval = None

class SLinkedList: # creating a head of the linked list 
    def __init__(self):
        self.headval = None

list1 = SLinkedList() # object declared and because of the contructor we have made a head node 
list1.headval = Node("Mon")
e1 = list1.headval
e2 = Node("Tue")
e3 = Node("wed")
e4 = Node("Wed")
# linking the nodes

e1.nextval = e2
e2.nextval = e3
e3.nextval = e4
