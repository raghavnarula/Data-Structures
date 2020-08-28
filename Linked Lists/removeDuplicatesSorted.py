import insertion,deletion,middleOfList
class List(deletion.List):
    def remove_duplicates_sorted(self):
        travel = self.headval

        while travel.nextval is not None:
            # compare the next element with current
            if (travel.dataval == travel.nextval.dataval):
                # deleting manually for time complexity rather than function
                travel.nextval = travel.nextval.nextval
                continue
            else:
                travel = travel.nextval

if __name__=='__main__':
    List1 = List()
    print("A with duplicates sorted list")
    List1.headval = insertion.Node(10)
    List1.insert(10)
    List1.insert(10)
    List1.insert(30)
    List1.insert(40)
    List1.print_list()
    List1.remove_duplicates_sorted()
    List1.print_list()
    print("Test case of normal list")
    List2 = List()
    List1.headval = insertion.Node(10)
    List1.insert(20)
    List1.insert(25)
    List1.insert(30)
    List1.insert(40)
    List1.print_list()
    
