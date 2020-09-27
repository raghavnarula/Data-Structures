import insertion
# print node lying at pth postion from element x
import sys
import time
class List(insertion.List):
    def node_lying(self,x,p):

        last = self.headval
        address = None
        if self.headval.dataval == x:
            address = self.headval
            print(address,address.dataval)
        else:
            while last.dataval != x:
                last = last.nextval
                # store the address of last in a variable
                address = last 
                print(address,address.dataval)
        print("Hello",last.dataval)
        for _ in range(p):
            last = last.nextval
            if last.nextval is None:
                last.nextval = self.headval
                time.sleep(3)

        print(address.dataval)
        print(last.dataval)
        address.nextval = last
        print("sucess!")
        self.print_list()

                        # if p lies outside the range

list1 = List()
list1.insert(1)
list1.insert(2)
list1.insert(3)
list1.insert(4)
list1.insert(5)
list1.insert(6)
list1.insert(7)
list1.node_lying(2,3)
list1.node_lying(2,2)
# list1.node_lying(1,10)




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