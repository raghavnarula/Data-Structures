# find the minimum element of the given stack with constant space n time
# first push an element
class Stack:
    def __init__(self):
        pass
    min_element = 0

    def push(self,stack,element):
        if len(stack) == 0:
            stack.insert(0,element)
            self.min_element = element
        else:
            if element >= self.min_element:
                #insert the element
                stack.append(element)
            
            else:
                # take the 2*x - min_element and insert that
                stack.append(2*element - self.min_element)
                #update the minimum
                self.min_element = element
        print(stack)
        
    def pop(self,stack):
        if stack[-1] > self.min_element:
            #pop element
            stack.pop()
        # if top is less than min then we know that element has changed here.
        else:
            # we have to update the minimum element and also remove it..
            self.min_element = 2*(self.min_element)-stack[-1]
            stack.pop()
        
        # print("The minimum element is :",self.min_element)
        print(stack)

    def get_min(self,stack):
        print("the minimum is:",self.min_element)

if __name__ == '__main__': 
    stack=[]
    s = Stack()
    s.push(stack,3)
    s.push(stack,5)
    s.push(stack,2)
    s.push(stack,1)
    s.push(stack,1)
    s.push(stack,-1)
    s.get_min(stack)
    s.pop(stack)
    s.get_min(stack)
    s.pop(stack)
    s.get_min(stack)
    s.pop(stack)
    s.get_min(stack)
    s.pop(stack)
    s.get_min(stack)
    s.pop(stack)
    s.get_min(stack)








