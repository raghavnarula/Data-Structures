import insertion,product_linked_list

list1 = product_linked_list.List()
list1.insert(10)
list1.insert(20)
list1.insert(30)
list1.insert(30)
list1.insert(20)
list1.insert(10)
list1.print_list()

# now we have made a linked list 10 20 30 30 20 10

class List(product_linked_list.List):
    def palindrome_check(self):
        # 2 pointers one moves at twice the speed
        fast = self.headval
        nor = self.headval

        while fast is not None:
            fast = fast.nextval.nextval
            nor = nor.nextval
        
        # now we make the linked lists into 2 
        # from start to normal and from normal to fast
        # reverse the linked list from normal to fast


        #now check from every element from frst linked list and second ll
        # compare them.
        
        

list1 = List()
list1.insert(10)
list1.insert(20)
list1.insert(30)
list1.insert(30)
list1.insert(20)
list1.insert(10)
list1.print_list()

list1.palindrome_check()
