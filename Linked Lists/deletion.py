import insertion
print("THe positions start from 0")

list1 = insertion.List()
list1.headval = insertion.Node(1) # when we are importing a class then we have to do 
list1.insertion_position(2,1)
list1.print_list()

class List(insertion.List):
    def deletion(self,position):
        node = self.headval
        if position == 0:
            self.headval = self.headval.nextval  # headnode
            return
        node = self.headval
        for _ in range(position-1):# 1 before the deletion
            node = node.nextval
        node.nextval = node.nextval.nextval

if __name__=='__main__':
    List1 = List()
    List1.headval = insertion.Node(10)
    List1.insertion_position(20,1)
    List1.insertion_position(30,2)
    List1.insertion_position(40,3)
    List1.print_list()
    List1.deletion(3)
    List1.print_list()



