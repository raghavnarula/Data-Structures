# Creating a doubly linked lists

import insertion,product_linked_list
class Node:
    def __init__(self,data):
        self.prevval = None
        self.dataval = data
        self.nextval = None
    
class List(product_linked_list.List): # inheriting from the class
    def insert_doubly(self,data): # inserts at the end
        # creating a new node 
        new_node = Node(data)

        if (self.headval is None):
            self.headval = new_node
            return
        else:
            # travel to the last node
            last = self.headval
            while(last.nextval is not None):
                last = last.nextval
            # now we are at the last node of the linked list
            last.nextval = new_node
            # connecting the previous of new_node to the last node in the linked list
            new_node.prevval = last
    
    def insert_begin_doubly(self,data):
        new_node = Node(data)
        new_node.nextval = self.headval
        self.headval.prevval=new_node
        self.headval = new_node
        return
    




if __name__ =="__main__":
    list1 = List()
    list1.insert_doubly(10)
    list1.insert_doubly(20)
    list1.insert_doubly(30)
    list1.print_list()
    list1.insert_begin_doubly(0)
    list1.print_list()
    list1.




