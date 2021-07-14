# we have to get the max gold
result = []
visited = set()
def no_more(board,x,y):
    if board[x][y] in visited or board[x][y]==0:
        return False
    return True


def algo(board,x,y):
    global final
    # ending case .. if no more position to go ..
    
    if no_more(board,x,y):
        board[x]
        print("here") 
        result.append(final)
        return

    else:
        for i in grid:
            for j in i:
                # grid[i][j] # starting point
                final += grid[i][j]
                visited.add(grid[i][j])
                
                print(grid[i][j],"hh")
                algo(board,x+1,y)
                algo(board,x-1,y)
                algo(board,x,y+1)
                algo(board,x,y-1)
            
            
        return False
    
board = [[1,0,7],
        [2,0,6],
        [3,4,5],
        [0,3,0],
        [9,0,20]]


algo(board,0,0)

print(result)
                
        
     