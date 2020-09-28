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
        last = self.headval
        if pos==0:
            NewNode.nextval = self.headval
            self.headval = NewNode
            return 
        else:
            for _ in range(pos-1):
                if last.nextval is not None:
                    last = last.nextval
            NewNode.nextval = last.nextval
            last.nextval = NewNode
    
    
    def insert_begin(self,dataval):
        NewNode = Node(dataval)
        self.list_nodes_storage.append(NewNode)
        NewNode.nextval = self.headval
        self.headval = NewNode

    def print_position(self,data):
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
        position = List.print_position(self,prev)
        List.insertion_position(self,data,position+1)
        
    def element_checker(self,data):
        
        last = self.headval
        while last is not None:
            if last.dataval == data:
                return True
            last = last.nextval
        return False

    def insert_before(self,data,after_element):
        # if we want to insert at the beginning
        last = self.headval
        if last.dataval == after_element: # first position.
            List.insert_begin(self,data)

        while last.nextval.dataval != after_element:
            last = last.nextval
        List.insert_specific(self,data,last.dataval)
        
    def insert_middle_between(self,start_number,end_number,data):

        start_pos = List.print_position(self,start_number)
        end_pos = List.print_position(self,end_number)
        middle = int((start_pos + end_pos)/2)
        List.insertion_position(self,data,middle+1)

    def circular_checker(self):
        last = self.headval
        while last is not self.headval or last is not None:
            if last.nextval == self.headval:
                return True
            elif last.nextval == None:
                return False
            last = last.nextval
        return False
    def node_between(self,x,p):
        # flag = 0
        last = self.headval
        if last.dataval == x:
            pass

        while last.dataval !=x:
            last = last.nextval
        address = last
        for _ in range(0,p):
            last = last.nextval
            if last.nextval == None:
                last.nextval = self.headval
                # flag = 1


        address.nextval = last

    def nodes_storage(self):
        print(self.list_nodes_storage)


    def node_pointer_counter(self):
        nodes = self.list_nodes_storage
        frequencies = {}        
        for node in nodes:
            if node.nextval in frequencies:
                frequencies[node.nextval] +=1
            else:
                frequencies[node.nextval] = 1
        count = 0
        value_list = []
        for key,value in frequencies.items():
            if value > 1:
                value_list.append(key)
                count += 1
        value_access = []
        for value in value_list:
            value_access.append(value.dataval)
        value_access.sort()

        return count         
    
    def value_nodes(self):
        nodes = self.list_nodes_storage
        frequencies = {}        
        for node in nodes:
            if node.nextval in frequencies:
                frequencies[node.nextval] +=1
            else:
                frequencies[node.nextval] = 1
        count = 0
        value_list = []
        for key,value in frequencies.items():
            if value > 1:
                value_list.append(key)
                count += 1
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


for i in range(number):
    list = input("").split(maxsplit=10)
    if list[0]=="I":
        if list[1] == '0':
            list1.insert(int(list[2]))

        if list[1] == '1':
            if list1.element_checker(int(list[2])) == True:
                list1.insert_specific(int(list[3]),int(list[2]))

            elif list1.element_checker(int(list[3])) == True:
                list1.insert_before(int(list[2]),int(list[3]))
                
        if list[1] == '2':
            list1.insert_middle_between(int(list[2]),int(list[3]),int(list[4]))      

    
    if list[0] == 'U':
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
