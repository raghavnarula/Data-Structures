# number of unique paths from 0,0 to n,m in a grid..

def grid(n,m):
    # if we are at n,m we are the end 
    # print((n,m),end=" ")
    if n<=1 or m<=1 :
        return 1
    else:
        return grid(n-1,m)+grid(m,n-1)


print(grid(3,3))