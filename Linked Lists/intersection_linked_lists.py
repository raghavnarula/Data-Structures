'''
Write a program to find the node at which the
intersection of two singly linked lists begins.
'''

# At least the next element must match for answer..

          # sucess
# 10 20 30 40 50 
# 0 5 15 30 40 50 

# unsuccessful
# 10 20 30 40 50 
# 0 5 15 30 35 60 




import insertion,length

count = 0
list1 = insertion.List()
list1.insert(20)
list1.insert(10)
list1.insert(5)
list1.insert(30)
list1.insert(40)
list1.insert(50)

list2 = insertion.List()
list2.insert(-10)
list2.insert(0)
list2.insert(5)
list2.insert(20)
list2.insert(15)
list2.insert(30)
list2.insert(40)
list2.insert(50)

list1.print_list()
list2.print_list()

val = 30
# after this value the nodes must have same value

temp1 = list1.headval
temp2 = list2.headval

while (temp1.dataval!=temp2.dataval):
    # move the pointer
    temp1 = temp1.nextval
    temp2 = temp2.nextval
    if (temp1 is None):
        temp1 = list2.headval
    if (temp2 is None):
        temp2 = list1.headval
    print(temp1.dataval,temp2.dataval)
    print(temp1,temp2)
    
    # we already have the solution by now
    if temp1.dataval == temp2.dataval:
        print("======================================================================================ATLEAST SOME FOUND")
        t1 = temp1
        t2 = temp2
        # checking the next elements are also matching 
        print("Check")
        while t1.nextval is not None:
            if t1.dataval != t2.dataval:
                print("we must continue")
                temp2 = temp2.nextval # Lets increase the value.
            t1 = t1.nextval
            t2 = t2.nextval
            # if the test fails eg -> 14567 1345787544 (2 lists match at start)
        print("Test Done!")
        # break
    count += 1
    
    # ending condition
    if (count>10000*length.List.length(list1)):
        print("No successive intersections for the linked lists")
        break


print(list1.print_position(temp1.dataval))
print(list2.print_position(temp2.dataval))
# now we have the element we have to find the position 


    





    
  




     




