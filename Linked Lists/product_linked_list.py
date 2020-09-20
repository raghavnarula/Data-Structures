# finding the product of 2 linked lists
import sys
import insertion,deletion,middleOfList



class List(middleOfList.List):
    def multiply_new(self,list):
    # create a new list for multiply
        list_product = insertion.List()
        if self.length() !=list.length():
            print("Multiplication cannot be done!",end=" ")
        else:
            #multiply the list
            last1 = self.headval
            last2 = list.headval
            while last1 is not None:
                x = (last1.dataval)*(last2.dataval)
                list_product.insert(x)
                last1 = last1.nextval
                last2 = last2.nextval
        return list_product.print_list()
    
    def multiply(self,list):
        # multiplication is done in the same linked list rather than creating a new one
        if self.length() !=list.length():
            print("Multiplication cannot be done!",end=" ")
        else:
            #multiply the list
            last1 = self.headval
            last2 = list.headval
            while last1 is not None:
                last1.dataval = (last1.dataval)*(last2.dataval)
                last1 = last1.nextval
                last2 = last2.nextval
        return self.print_list()


if __name__ =="__main__":
    list1 = List()
    list1.insert(10)
    list1.insert(20)
    list1.insert(30)


    list2 = List()
    list2.insert(0)
    list2.insert(0)
    # list2.insert(0)

    list1.multiply_new(list2)

    list4 = List()
    list4.insert(30)
    list4.insert(50)
    list4.insert(50)

    list5 = List()
    list5.insert(3)
    list5.insert(3)
    list5.insert(3)

    list4.multiply_new(list5)
 
    # changes in the same linked list 
    list6 = List()
    list6.insert(30)
    list6.insert(50)
    list6.insert(50)

    list7 = List()
    list7.insert(3)
    list7.insert(3)
    list7.insert(3)

    list6.multiply(list7)