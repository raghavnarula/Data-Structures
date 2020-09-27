# insertion in linked list is very key thing.

# here we are inserting the in list only at the first and last position.
class Node:
    def __init__(self,dataval):
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
    def insertion_begin(self,dataval):
        NewNode = Node(dataval)
        NewNode.nextval = self.headval
        self.headval = NewNode

    def insert(self,dataval): # this inserts at the end
        NewNode = Node(dataval)
        # print(NewNode,NewNode.dataval) printing extra info about the node
        if self.headval is None:
            self.headval = NewNode
            return 
        else:
            last = self.headval 
            # iterate to last node address
            while last.nextval is not None:
                last = last.nextval
            last.nextval = NewNode
        return 0
        
    def print_at_position(self,pos):
        last = self.headval
        for _ in range(pos): 
            last = last.nextval
        return last.dataval

    # insertion at specific position
    def insertion_position(self,data,pos):
        NewNode = Node(data)
        # print(NewNode,NewNode.dataval) printing info about the node
        last = self.headval
        if pos==0:
            NewNode.nextval = self.headval
            self.headval = NewNode
            return 
        else:
            for _ in range(pos-1):
                if last.nextval is not None:
                    last = last.nextval
        # now we are 1 position before the place where we want to insert
            NewNode.nextval = last.nextval
            last.nextval = NewNode
    
    def print_position(self,data):
        # finding the positions of the elements 
        last = self.headval
        count = 0
        while (last is not None):
            if last.dataval == data:
                return count
            count +=1
            last = last.nextval
    
    def insert_middle(self,data):
        # inserts the element at the middle of the linked list
        # 1 2 3 4 5 (insert 10)
        # 1 2 3 10 4 5 
        # or 
        # 1 2 4 5 (insert 3)
        # 1 2 3 4 5
        fast = self.headval.nextval
        slow = self.headval
        while fast is not None and fast.nextval is not None:
            fast = fast.nextval.nextval
            slow = slow.nextval
        # now insert at the position next to slow pointer
        new_node = Node(data)
        new_node.nextval = slow.nextval
        slow.nextval = new_node
    def insert_middle_between(self,start_number,end_number,data):
        # start and end must not be repeating in the linked lists
        # find the position of start and end
        start_pos = List.print_position(self,start_number)
        end_pos = List.print_position(self,end_number)
        print(start_pos,end_pos)
        middle = int((start_pos + end_pos)/2)
        print(middle)
        List.insertion_position(self,data,middle+1)
        

if __name__=='__main__':
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
    list1.insert(4)
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

    list3 = List()
    list3.insert(10)
    list3.insert(20)
    list3.insert(30)
    list3.insert(40)
    list3.insert(60)
    list3.insert(70)
    list3.insert(80)

    list3.print_list()
    # print(list3.print_position(80))
    list3.insert_middle_between(40,60,50)
    list3.print_list()