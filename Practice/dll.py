class Node:
    def __init__(self,data):
        self.dataval = data
        self.nextval = None
    
class LinkedList:
    def __init__(self):
        self.headval = None
    def insert(self,value):
        if  self.headval == None:
            #insert in the head position
            self.headval = Node(value)
        else:
            # traverse to the end position
            temp = self.headval
            print("type")
            while temp.nextval is not None:
                temp = temp.nextval
            # now we are at the last position in the linked list
            # Insertion takes place
            temp.nextval = Node(value)
        
    def printing(self):
        temp = self.headval
        while temp is not None:
            print(temp.dataval,end=" ")
            temp = temp.nextval
        print(" ")

linkedList = LinkedList()
linkedList.insert(10)
linkedList.insert(20)
linkedList.insert(30)
linkedList.insert(40)
linkedList.insert(50)
linkedList.printing()
