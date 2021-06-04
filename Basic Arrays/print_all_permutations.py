a = input()
b = list(a)


# choices 
'''
we have choices of 3 letters 
'''
# constraints
'''
we have no constraints
'''
# goal
'''
find all strings
'''
def toString(b):
    print( "".join(b))

def helper(b,start,end):
    # b is a list

    # ending
    if start == end:
        return toString(b)
    else:
        for i in range(start,end+1):
            # we make cases
            # print(f"chaging the {b[i]} and  {b[start]}")
            b[i] , b[start] = b[start] , b[i]

            # now we have to move forward and repeat the same step with less 
            helper(b,start +1,end)
            # backtracking condition
            # if we dont get the required free up the space also i mean return to original
            b[i] , b[start] = b[start] , b[i]

print(helper(b,0,len(b)-1))









