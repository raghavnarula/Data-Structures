import insertion
# print node lying at pth postion from element x
import sys

class List(insertion.List):
    def node_between(self,x,p):
        flag = 0
        # first find the position of x
        last = self.headval
        if last.dataval == x:
            print("at first position")
            # store the address of the last.nextval will be used later

        while last.dataval !=x:
            last = last.nextval
        # now we are on the element x node
        # print(last.dataval)
        address = last
        print(address.dataval,address)
        for _ in range(0,p):
            # count p positions from last
            # print(_,end=" ")
            last = last.nextval
        # now we are at p positions away from address
            if last.nextval == None:
                last.nextval = self.headval
                flag = 1


        address.nextval = last

        if flag == 0:
            pre = self.headval
            while pre is not None:
                print(pre.dataval,end = " ")
                pre = pre.nextval
            print()
        else:
            pre = self.headval
            while True:
                print(pre.dataval,end = " ")
                pre = pre.nextval
                if pre ==self.headval:
                    break
            print()

        


                        # if p lies outside the range

list1 = List()
list1.insert(1)
list1.insert(2)
list1.insert(3)
list1.insert(4)
list1.insert(5)
list1.insert(6)
list1.insert(7)
list1.node_between(2,3)
list1.node_between(2,2)
list1.node_between(1,6)



# for j in range(p):
        #     last = last.nextval
        #     # if reaching the last node make it circular
        #     print(last.dataval) 
        #     if last.nextval is None: # and the loop is still on we have to make a circular linked lists
        #         last.nextval = self.headval
        #         # run the loop for j to p now
        #         print(j)
        #         for _ in range(j,p):
        #             last = last.nextval
        #         # sys.exit()
        #         break
    

    # def node_lying(self,x,p):
    #     last = self.headval
    #     address = None
    #     if self.headval.dataval == x:
    #         address = self.headval
    #         print(address,address.dataval)
    #     else:
    #         while last.dataval != x:
    #             last = last.nextval
    #             # store the address of last in a variable
    #             address = last 
    #             print(address,address.dataval)
    #     print("Hello",last.dataval)
    #     for _ in range(p):
    #         last = last.nextval
    #         if last.nextval is None:
    #             last.nextval = self.headval

    #     print(address.dataval)
    #     print(last.dataval)
    #     address.nextval = last
    #     print("sucess!")
    #     self.print_list()
'''
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
            print()
            print(last.dataval,"pointing to :",last.nextval,end =" ")
            last = last.nextval
            i += 1
        print(" ")
        '''          