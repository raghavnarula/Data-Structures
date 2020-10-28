'''
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
'''

stack = []
s = input()
match = {
    '(':')',
    '[':']',
    '{':'}'
}


def valid(s):
    count = 0
    for par in s:
        if par == "(" or par == "{" or par == "[":
            stack.append(par)
        else:
            # handling the closing brackets
            if match[stack.pop()] != par:
                return False
        
        # also check if the stack is empty or not
    if len(stack) == 0:
        return True
    else:
        return False

            
            

print(valid(s))