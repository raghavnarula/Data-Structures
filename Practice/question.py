class Node:
    def __init__(self,data):
        self.dataval = data
        self.nextval  = None
    
class LinkedList:
    def __init__(self):
        self.headval = None
        self.l2 = None
        self.l3 = None

    def insert(self,value):
        if  self.headval == None:
            #insert in the head position
            self.headval = Node(value)
        else:
            # traverse to the end position
            temp = self.headval
            while temp.nextval is not None:
                temp = temp.nextval
            # now we are at the last position in the linked list
            # Insertion takes place
            temp.nextval = Node(value)
        
    def insertion_position(self,value,position):
        # eg position is n then we have to travel to the n-1 the position and we are starting from 0 (remember that thing)
        if position==0:
            first = Node(value)
            first.nextval = self.headval
            self.headval = first
        else:
            temp = self.headval
            for _ in  range(position-1):
                temp = temp.nextval
            # Now we are at the 1 position before
            insertion = Node(value)
            insertion.nextval = temp.nextval
            temp.nextval = insertion

    def printing(self):
        temp = self.headval
        while temp is not None:
            print(temp.dataval,end=" ")
            temp = temp.nextval
        print(" ")
    
    def LL2(self):
        n = int(self.length_ll() / 2)
        # create a new linked list 
        # odd ka sum
        ll2 = LinkedList()
        temp = self.headval
        for _ in range(n-1):
            sum = temp.dataval + temp.nextval.nextval.dataval
            # create a node sum that places in it 
            ll2.insert(sum)
            temp = temp.nextval.nextval
            print("temp",temp.dataval)
        print("Printing the list 2")
        self.l2 = ll2.headval
        ll2.printing()
    
    def LL3(self):
        n = int(self.length_ll() / 2)
        # create a new linked list 
        # even ka sum
        ll3 = LinkedList()
        temp = self.headval.nextval
        for _ in range(n-1):
            sum = temp.dataval + temp.nextval.nextval.dataval
            # create a node sum that places in it 
            ll3.insert(sum)
            temp = temp.nextval.nextval
        print("Printing the list 3")
        ll3.printing()
    
    def length_ll(self):
        temp = self.headval
        length = 0
        while temp is not None:
            length += 1
            temp = temp.nextval
        return int(length)
    
    def median(self):
        # First add the middle node
        temp = self.headval
        first = self.headval
        while temp.nextval is not None:
            temp = temp.nextval
        sum = first.dataval + temp.dataval
        # insert this node at the middle of the linked list
        linkedList.insertion_position(sum,int(linkedList.length_ll()/2))

        # after calculating the mid position that is 3 
        mid = int(linkedList.length_ll()/2)
        print("value of mid")
        current = self.l2
        next = self.l2.nextval
        temp = self.headval
        for _ in range(mid): # take l2 and insert it
           # merge the current in the list1
            current.nextval = temp.nextval
            temp.nextval = current
            

            
linkedList = LinkedList()
linkedList.insert(1)
linkedList.insert(2)
linkedList.insert(3)
linkedList.insert(4)
linkedList.insert(5)
linkedList.insert(6)
linkedList.length_ll()
linkedList.printing()
# print(linkedList.headval)
linkedList.LL2()
linkedList.LL3()
linkedList.median()
linkedList.printing()

print(linkedList.l2.nextval.dataval)
