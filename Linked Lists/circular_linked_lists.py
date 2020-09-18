###########################################################################
#        Circular linked Lists creation from a singly linked list         #
###########################################################################

# most  previous codes created will not work in circular linked list beacause of never ending loops

import insertion,deletion,middleOfList
class List(middleOfList.List):
    def circular_insertion(self,data):
        new = insertion.Node(data)
        
        # connect the new node to previous linked list
        last = self.headval
        while last.nextval is not None:
            last = last.nextval
        last.nextval = new
        new.nextval = self.headval # linking the last node to the headnode
    
    # length function for circular linked list
    def length_circular(self):
        last = self.headval.nextval
        # count = 0
        length = 1
        while last is not self.headval:
            length +=1
            last = last.nextval
        return int(length)

    # Printing the circular linked lists 
    def print_list_circular(self):
        len = List.length_circular(self)
        last = self.headval
        i = 0
        while i < len:
            print(last.dataval,end =" ")
            last = last.nextval
            i += 1
        print(" ")  

if "__main__"==__name__:
    list = List()
    list.insert(230)
    list.insert(240)
    list.insert(250)
    list.insert(260)
    list.circular_insertion(270)
    # list.insert(280)
    list.length_circular()
    list.print_list_circular()
