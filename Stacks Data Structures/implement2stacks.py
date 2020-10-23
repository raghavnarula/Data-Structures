'''
Make 2 stacks in the same array
           ---------------------------------------
stack 1--> |  |   |   |   |   |   |   |   |   |   | <---stack 2
           ---------------------------------------
'''
class twoStacks:
    def __init__(self,n):
        self.size = n
        self.arr = [None]*n # list of None created
        self.top1 = -1 # starting from position -1 , we must catch from position 0 but heres a catch
        self.top2 = self.size # starting from position nth position , we must start from n-1 as we might think but here is a catch.

        '''
        We start from 1 position behind the starting position because we have to increment the top . 
        At the end if we start from position 0 or n-1 then the top would be null and nothing would get printed.(if we print the top)
        '''
    
    def checker(self): # to check if we can insert or not
        if self.top2 > self.top1 + 1:
            print("We can insert")
        else:
            print("Stack overflow will occur now!")

    def push_stack1(self,x):
        if self.top1 < self.top2 - 1:
            self.top1 = self.top1 + 1
            #insert the element in arr at position top1
            self.arr[self.top1] = x
        else:
            print("stack overflow")

    def push_stack2(self,x):
        if self.top2 > self.top1 + 1:
            self.top2 = self.top2 - 1
            # insert the element
            self.arr[self.top2] = x
        else:
            print("Stack overflow")
    
    def pop_stack1(self):
        self.arr[self.top1] = None
    
    def pop_stack2(self):
        self.arr[self.top2] = None
        

s = twoStacks(10)
print(s.arr)
s.push_stack1(10)
print(s.arr)
s.push_stack1(20)
print(s.arr)
s.push_stack1(30)
print(s.arr)
s.push_stack1(40)
print(s.arr)
s.push_stack1(50)
print(s.arr)
s.push_stack1(60)
print(s.arr)
print(s.top1,s.top2)
s.push_stack2(100)
print(s.arr)
print(s.top1,s.top2)
s.push_stack2(90)
print(s.arr)
s.checker()
print(s.top1,s.top2)
s.push_stack2(80)
print(s.arr)
s.checker()
print(s.top1,s.top2)
s.push_stack2(70)
print(s.arr)
s.checker()
print(s.top1,s.top2)
s.push_stack2("None")
print(s.arr)
s.checker()
print(s.top1,s.top2)
s.checker()
s.pop_stack1()
print(s.arr)




