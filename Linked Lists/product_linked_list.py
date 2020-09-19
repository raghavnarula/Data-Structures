# finding the product of 2 linked lists
import sys
import insertion,deletion,middleOfList

list3 = insertion.List()


class List(middleOfList.List):
    def multiply(self,list):
        if self.length() !=list.length():
            print("Multiplication cannot be done!",end=" ")
        else:
            #multiply the list
            last1 = self.headval
            last2 = list.headval
            while last1 is not None:
                x = (last1.dataval)*(last2.dataval)
                list3.insert(x)
                last1 = last1.nextval
                last2 = last2.nextval
        return 

list1 = List()
list1.insert(10)
list1.insert(20)
list1.insert(30)



list2 = List()
list2.insert(0)
list2.insert(0)
# list2.insert(0)

list1.multiply(list2)
list3.print_list()