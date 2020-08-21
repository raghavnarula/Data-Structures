# insertion in linked list is very key thing.

# here we are inserting the in list only at the first and last position.
    
class Node:
    def __init__(self,dataval=None):
        self.dataval = dataval
        self.nextval = None

class List:
    def __init__(self):
        self.headval = None

    def print_list(self):
        printval = self.headval
        while printval is not None:
            print(printval.dataval,end =" ")
            printval = printval.nextval
        print(" ")
    def insertion_begin(self,new_data):
        NewNode = Node(new_data)
        NewNode.nextval = self.headval
        self.headval = NewNode

    def insertion_end(self,data_val):
        NewNode = Node(data_val)
        if self.headval is None:
            self.headval = NewNode
            return
        else:
            last = self.headval 
            # iterate to last node address
            while last.nextval is not None:
                last = last.nextval
            last.nextval = NewNode
    def print_at_position(self,pos):
        last = self.headval
        for _ in range(pos): 
            last = last.nextval
        print(f"At position {pos} we have,{last.dataval}")

    # insertion at specific position
    def insertion_position(self,data,pos):
        NewNode = Node(data)
        last = self.headval
        if pos==0:
            NewNode.nextval = self.headval
            self.headval = NewNode
        else:
            for _ in range(pos-1):
                if last.nextval is not None:
                    last = last.nextval
        # now we are 1 position before the place where we want to insert
            NewNode.nextval = last.nextval
            last.nextval = NewNode
        


    
list1 = List()
list1.headval = Node(1)
n1 = list1.headval
n2 = Node(2)
n3 = Node(3)
n1.nextval = n2
n2.nextval = n3

list1.print_list()
list1.insertion_begin(0)
list1.print_list()
list1.insertion_end(4)
list1.print_list()
list1.print_at_position(2)
list1.insertion_position("Tue",3)
list1.print_list()

list2 = List()
list2.headval = Node("Mon")
list2.insertion_position("Tue",1)
list2.insertion_position("Wed",2)
list2.print_list()
list2.insertion_position(2,0) #list2.insertion_begin(2)
list2.print_list()



