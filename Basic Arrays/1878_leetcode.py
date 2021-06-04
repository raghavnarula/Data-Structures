grid = [[3, 4, 5, 1, 3], [3, 3, 4, 2, 3], [20, 30, 200, 40, 10], [1, 5, 5, 4, 1], [4, 3, 2, 2, 5]]
# grid = [[1,2,3],[4,5,6],[7,8,9]]
grid = [[7,7,7]]
final = set()

m = len(grid[0]) # row
n = len(grid) # column
# size 2 waale saare
## This is for square grid only.
for alpha in range((min((m+1)//2, (n+1)//2))):
    # we have to select bita and pi such that all cases are done 
    # selecting the max of bita and pi we get 
    for row in range(alpha,m-alpha):
        for column in range(alpha,n-alpha):
            if alpha==0:
                print(row,column)
                # sum = grid[row][column]
                sum = grid[column][row]
            else:
                sum = 0
                for j in range(alpha):
                    sum += grid[column-alpha+j][row+j]
                    sum += grid[column+j][row+alpha-j]
                    sum += grid[column+alpha-j][row-j]
                    sum += grid[column-j][row-alpha+j]
            final.add(sum)

print (sorted(final,reverse=True)[:3])