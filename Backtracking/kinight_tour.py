# solving the famous knight tour problem
'''
If all squares are visited 
    print the solution
Else
   a) Add one of the next moves to solution vector and recursively 
   check if this move leads to a solution. (A Knight can make maximum 
   eight moves. We choose one of the 8 moves in this step).
   b) If the move chosen in the above step doesn't lead to a solution
   then remove this move from the solution vector and try other 
   alternative moves.
   c) If none of the alternatives work then return false (Returning false 
   will remove the previously added item in recursion and if false is 
   returned by the initial call of recursion then "no solution exists" )
'''
# size of the board
n=3

def isSafe(x,y,board):
    # this is a function to check if the the valid indexes of the problem.
    if (x>=0 and y>=0 and x<n and y<n and board[x][y]==-1):
        return True
    return False

def print_board(n,board):
    for i in range(n):
        for j in range(n):
            print(board[i][j],end=" ")
        print()



def algorithm(n):
    # initializing the board
    board = [[-1 for i in range(n)]for i in range(n)] # printing -1 to all places in the board..

    # move x and y defining the next move of the knight 
    '''
    There are 8 possible options 2 1 -1 -2 in it .
    '''
    move_x = [2,1,-1,-2,2,1,-1,-2]
    move_y = [1,2,2,1,-1,-2,-2,-1]

    # Since the Knight is initially at the first block 
    board[0][0] = 0

    # step counter for the knight
    pos = 1

    if(main_algo(n,board,0,0,move_x,move_y,pos)==False):
        print("Solution Does not exists")
    
    else:
        print_board(n,board)

def main_algo(n,board,curr_x,curr_y,move_x,move_y,pos):
    
    if (pos == n**2):
        return True
    for i in range(8): # relevant positions in the move_x
        new_x = curr_x + move_x[i] 
        new_y = curr_y + move_y[i] 
        if(isSafe(new_x,new_y,board)): 
            board[new_x][new_y] = pos 
            if(main_algo(n,board,new_x,new_y,move_x,move_y,pos+1)): 
                return True
              
            # Backtracking 
            # print_board(n,board)
            board[new_x][new_y] = -1
    return False

if __name__ == '__main__':
    algorithm(n)



'''
Analysing the problem 
what we did ?
firsty we created a board that was initialized with -1 like a 2d array.. n*n

Then we chose a starting position that is 0,0 on the board from where we will be starting it.
now we have only n*n positions to move on the board . if that exceeds then we have to terminate the things.

else we have to take all the valid moves of the knight . there are 8 positions at max thorugh which it can move
new_pos = current postiion + move_coordinate

checking if that move is valid or not.

if valid then we write the position number on the board .
and then again start doing it recursively.
'''

