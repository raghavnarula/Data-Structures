import deletion,insertion


class List(deletion.List):
    def length(self):
        count = 0
        traverse = self.headval
        while traverse is not None:
            count += 1
            traverse = traverse.nextval
        return count 

if __name__ == '__main__':
    List1 = List()
    List1.headval = insertion.Node(10)
    List1.insertion_position(20,1)
    List1.insertion_position(30,2)
    List1.insertion_position(40,3)
    List1.print_list()
    a = List1.length()
    print(a)
    print(f"the length of the list is: {List1.length()}")

