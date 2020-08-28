import length,insertion

class List(length.List):
    def middle(self):
        a = int(List.length(self))
        middle = (0 + a) // 2
        if middle%2 == 0:
            element = List.print_at_position(self,middle-1)
        else:
            element = List.print_at_position(self,middle)
        return element

if __name__ == '__main__':
    List1 = List()
    List1.headval = insertion.Node(10)
    List1.insertion_position(20,1)
    List1.insertion_position(30,2)
    List1.insertion_position(40,3)
    # List1.insertion_position(50,5)
    List1.print_list()
    print(List1.middle())
    # print(f"the middle of the list is: {List1.middle()}")