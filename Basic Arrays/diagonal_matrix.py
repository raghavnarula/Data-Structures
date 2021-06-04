# check wheather the matrix is diagonal or not

## -> 

a = [[1,0,1],[0,5,0],[0,0,9]]

def diagonal(a): # a is the matrix
    for i in range(3): # number of rows
        for j in range(3): # number of columns
            if a[i][j] == 0 and i != j:
                pass
            elif a[i][j] == 0 and i == j:
                print("Not a diagonal matrix")
                return 
            elif a[i][j] != 0 and i!= j:
                print("Not a diagonal matrix")
                return
    print("Its A diagonal")
    return

def tridiagonal(a):
    # One diagonal above and one diagonal below are present and not zero
    pass


diagonal(a)