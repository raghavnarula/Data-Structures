class Node:
    def __init__(self,data):
        self.dataval = data
        self.nextval  = None
    
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
            self.headval = first # update the head also
        else:
            temp = self.headval
            for _ in range(position-1):
                temp = temp.nextval
            # Now we are at the 1 position before
            insertion = Node(value)
            insertion.nextval = temp.nextval
            temp.nextval = insertion

    def deletion(self,position):
        temp = self.headval
        print("headval",temp.dataval)
        for _ in range(position-1):
            temp = temp.nextval
        if position == 0:
            self.headval = self.headval.nextval
        elif temp.nextval is not None and position is not 0:
            temp.nextval = temp.nextval.nextval

    def printing(self):
        temp = self.headval
        while temp is not None:
            print(temp.dataval,end=" ")
            temp = temp.nextval
        print(" ")

    def reverse(self):
        previous = None
        next = None
        current = self.headval
        while current is not None:
            next = current.nextval
            current.nextval = previous
            previous = current
            current = next
        self.headval = previous
    
linkedList = LinkedList()
linkedList.insert(10)
linkedList.printing()
linkedList.insert(20)
linkedList.printing()
linkedList.insert(30)
linkedList.printing()
linkedList.insert(40)
linkedList.printing()
linkedList.insertion_position(100,2)
linkedList.printing()
linkedList.deletion(4)
linkedList.printing()
linkedList.reverse()
linkedList.printing()
linkedList.insertion_position(1000,0)
linkedList.printing()
linkedList.deletion(0)
linkedList.printing()