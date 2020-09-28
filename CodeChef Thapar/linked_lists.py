'''
Implement a singly linked list having all unique elements with the following operations.

I 0 x – Inserts element x at the end.
I 1 y x – If the element y exists, then insert element x after the element y, else insert element y before the existing element x.
Assuming either the element x or the element y exists.
I 2 z y x – Inserts element x in the middle of the elements z and y. The element z appears before the element y.
U x p – Links the next pointer of the element x to the node lying at the pth position from the element x while traversing towards right. 
In case of insufficient number of nodes,the counting continues by updating the existing linked list to its circular version.

Input:
Line 1 contains an integer N indicating the total number of operations.
Each of the following N lines contains an operation to be performed in the format as is described above.

Output:
Line 1 has 1 if the linked list gets updated to its circular version, else 0.
Line 2 has a count of the number of nodes whose addresses are contained in the next pointer of multiple nodes. 
If output at Line 2 is zero then output Line 4 will not be printed.
Line 3 has space separated contents of all the nodes which are counted to get the output at Line 2 in increasing order.
If output at Line 2 is zero then output Line 3 will have space separated contents of the generated linked list.
Line 4 has space separated respective frequencies of each output value, say x, at Line 3. 
'Frequency of each output value x' means the count of multiple nodes whose next pointers have address of a node with this value x.
Constraints
All integers range in between 1 and 1000.

Sample Input I:
3
I 0 1
I 1 1 7
I 2 1 7 3

Sample Output I:
0
0
1 3 7

EXPLANATION I:

Linked list after execution of each of the three operations given in the input is shown below.
1
1 - > 7
1 - > 3 - > 7

Sample Input II:
10
I 0 1
I 0 7 
I 1 6 7
I 1 1 2
I 2 1 7 3
I 2 3 6 5
I 2 1 7 4
U 2 3
U 2 2
U 1 6

Sample Output II:
1
1
6
3
'''
class Node:
    def __init__(self,data):
        self.dataval = data
        self.nextval = None

class List:
    def __init__(self):
        self.headval = None
        self.list_nodes_storage = []


    def insert(self,dataval):
        NewNode = Node(dataval)
        self.list_nodes_storage.append(NewNode)
        # print(NewNode,NewNode.dataval) printing extra info about the node
        if self.headval is None:
            self.headval = NewNode
            return 
        else:
            last = self.headval 
            # iterate to last node address
            while last.nextval is not None:
                last = last.nextval
            last.nextval = NewNode
        return 0
    
    def insertion_position(self,data,pos):
        NewNode = Node(data)
        self.list_nodes_storage.append(NewNode)
        # print(NewNode,NewNode.dataval) printing info about the node
        last = self.headval
        if pos==0:
            NewNode.nextval = self.headval
            self.headval = NewNode
            return 
        else:
            for _ in range(pos-1):
                if last.nextval is not None:
                    last = last.nextval
        # now we are 1 position before the place where we want to insert
            NewNode.nextval = last.nextval
            last.nextval = NewNode

    def print_position(self,data):
        # finding the positions of the elements 
        last = self.headval
        count = 0
        while (last is not None):
            if last.dataval == data:
                return count
            count +=1
            last = last.nextval
        return False
    
    def print_list(self):
        printval = self.headval
        while printval is not None:
            print(printval.dataval,end =" ")
            printval = printval.nextval
        print(" ")
    

    def insert_specific(self,data,prev):
        # insert data after element marked prev
        # first find the position of the prev
        # find the position of the element. then 
        position = List.print_position(self,prev)
        # print("the position at which the node is to be inserted",position+1)
        # now have to insert after this position
        List.insertion_position(self,data,position+1)
        
    def element_checker(self,data):
        # checks the present element is present or not
        last = self.headval
        while last is not None:
            if last.dataval == data:
                # print('Yes it exits')
                return True
            last = last.nextval
        return False

    def insert_before(self,data,after_element):
        # insert the data before the after element
        last = self.headval
        while last.nextval.dataval != after_element:
            last = last.nextval
        # now insert the element after the where last is now.
        List.insert_specific(self,data,last.dataval)
        
    def insert_middle_between(self,start_number,end_number,data):

        start_pos = List.print_position(self,start_number)
        end_pos = List.print_position(self,end_number)
        # print(start_pos,end_pos)
        middle = int((start_pos + end_pos)/2)
        # print(middle)
        List.insertion_position(self,data,middle+1)

    def circular_checker(self):
        last = self.headval
        # print(last.dataval)
        while last is not self.headval or last is not None:
            if last.nextval == self.headval:
                print("circular detected")
                return True
            elif last.nextval == None:
                return False
            last = last.nextval
        return False
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
        # print(address.dataval,address)
        for _ in range(0,p):
            # count p positions from last
            # print(_,end=" ")
            last = last.nextval
        # now we are at p positions away from address
            if last.nextval == None:
                last.nextval = self.headval
                flag = 1


        address.nextval = last

        # if flag == 0:
        #     pre = self.headval
        #     while pre is not None:
        #         print(pre.dataval,end = " ")
        #         pre = pre.nextval
        #     print()
        # else:
        #     pre = self.headval
        #     while True:
        #         print(pre.dataval,end = " ")
        #         pre = pre.nextval
        #         if pre ==self.headval:
        #             break
        #     print()
        address.nextval = last


    def nodes_storage(self):
        print(self.list_nodes_storage)


    def node_pointer_counter(self):
        # at all the nodes take the address value and 
        nodes = self.list_nodes_storage
        frequencies = {}        
        for node in nodes:
            if node.nextval in frequencies:
                frequencies[node.nextval] +=1
            else:
                frequencies[node.nextval] = 1
        # print(frequencies)
        # final = None
        count = 0
        value_list = []
        for key,value in frequencies.items():
            if value > 1:
                value_list.append(key)
                count += 1
        # print(count)
        # now we need to access the values at given nodes 
        value_access = []
        for value in value_list:
            value_access.append(value.dataval)
        value_access.sort()
        # now we have the sorted list of the values that are having freq more than 1

        return count         
    
    def value_nodes(self):
            # at all the nodes take the address value and 
        nodes = self.list_nodes_storage
        frequencies = {}        
        for node in nodes:
            if node.nextval in frequencies:
                frequencies[node.nextval] +=1
            else:
                frequencies[node.nextval] = 1
        # print(frequencies)
        # final = None
        count = 0
        value_list = []
        for key,value in frequencies.items():
            if value > 1:
                value_list.append(key)
                count += 1
        # print(count)
        # now we need to access the values at given nodes 
        value_access = []
        for value in value_list:
            value_access.append(value.dataval)
        value_access.sort()
        for val in value_access:
            print(val,end =" ")
        print()
    def frequency_printer(self):
        nodes = self.list_nodes_storage
        frequencies = {}        
        for node in nodes:
            if node.nextval in frequencies:
                frequencies[node.nextval] +=1
            else:
                frequencies[node.nextval] = 1
        # print(frequencies)
        # {Node:freq}
        # final = None
        count = 0
        value_list = [] # contains node that have freq > 1
        for key,value in frequencies.items():
            if value > 1:
                value_list.append(key)
                count += 1

        value_access = [] # contains all the node values inc order with freq>1
        for value in value_list:
            value_access.append(value.dataval)
        value_access.sort()
        value_freq_list = []
        
        for val in value_access:
            for node,freq in frequencies.items():
                if node.dataval ==val:
                    value_freq_list.append(freq)
        
        for frequency in value_freq_list:
            print(frequency,end =" ")
        print()



number = int(input(""))

list1 = List()
# list1.insert(1)
# list1.insert(2)
# list1.insert(3)
# list1.insert(4)
# list1.insert(5)
# list1.insert(6)
# list1.insert(7)

for i in range(number):
    list = input("").split(maxsplit=10)
    if list[0]=="i":
        if list[1] == '0':
            list1.insert(int(list[2]))

        if list[1] == '1':
            if list1.element_checker(int(list[2])) == True:
                list1.insert_specific(int(list[3]),int(list[2]))

                # the new element is inserted
            elif list1.element_checker(int(list[3])) == True:
                list1.insert_before(int(list[2]),int(list[3]))
                
        if list[1] == '2':
            list1.insert_middle_between(int(list[2]),int(list[3]),int(list[4]))      

    
    if list[0] == 'u':
        list1.node_between(int(list[1]),int(list[2]))

if list1.circular_checker() == True:
    print(1)
else:
    print(0)

print(list1.node_pointer_counter())

if list1.node_pointer_counter() == 0:
    list1.print_list()

if list1.node_pointer_counter() != 0:
    list1.value_nodes()

if list1.node_pointer_counter() != 0:
    list1.frequency_printer()
    

