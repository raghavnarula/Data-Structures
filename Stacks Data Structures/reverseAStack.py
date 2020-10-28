'''
Make 2 stack
           ---------------------------------------
stack 1--> |4  | 6  | 7  | 8  |  9 | 1  | 1  |   |  <- Insertion happens from here
           ---------------------------------------
             ^   
             |
            Top 
    After removal
           ---------------------------------------
stack 1--> |  6  | 7  | 8  |  9 | 1  | 1  |   |  
           ---------------------------------------
             ^   
             |
            Top 

pop till the last element of the stack and then insert at the end
'''
## inserts the element at the bottom of the stack
class Stack:
    top = 0
    def insertAtBottom(self,stack,element):
        stack.insert(0,element)
    def pop_first(self,stack):
        stack.pop(Stack.top)
        Stack.top = Stack.top+1
    def display(self,stack):
        print(stack)    
    
    def reverse(self,stack):
        # all items are held in function call till the time recursion finishes its task
        if len(stack)== 0:
            return
        
        else:
            a = stack.pop() # element has poped out
            Stack.reverse(self,stack)
            Stack.insertAtBottom(self,stack,a)
            





if __name__=='__main__':
    stack = []
    s = Stack()
    s.insertAtBottom(stack,10)
    s.insertAtBottom(stack,20)
    s.insertAtBottom(stack,30)
    s.insertAtBottom(stack,40)
    s.insertAtBottom(stack,50)
    s.display(stack)
    print("Top is at:",s.top)
    # s.pop_first(stack)
    s.display(stack)
    print("Top is at:",s.top)


    print("Now we are reversing the stack")
    s.reverse(stack)
    s.display(stack)
    







