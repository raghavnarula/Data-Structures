# finding the length of the stack using recursion

# if the stack becomes empty then we have to finish counting


def is_empty(stack):
    try:
        stack.pop()
        print("Not True")
    except IndexError:
        return True

count = 1
def leng(stack):
    if is_empty(stack) == True:
       return

    else:
        global count
        count = count + 1
        stack.pop()
        return leng(stack)    


l = [10,20]
leng(l)
print(count)

l = [10,20,30]
print(type(l.pop()))
print(l)
l.pop()
print(l)