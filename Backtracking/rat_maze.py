# similar to knights move problem this is problem in which the rat,has to get out of the maze. 
# the rat can move only through forward and backward and cannot cross the dead ends
# Taken reference from https://www.geeksforgeeks.org/rat-in-a-maze-backtracking-2/
n=4

def is_safe(x,y,n): # checking the validness of the move
    if (0<=x<n and 0<=y<n and maze[x][y]==1): # valid move 
        return True

def print_maze(sol): # printing the path
    for i in sol:
        for j in i:
            print(j,end=" ")
        print()

def algorithm(n,maze): # making the main algo work
    sol = [ [ 0 for j in range(n) ] for i in range(n) ] # creating the maze

    if(main_algo(maze,1,0,sol)==False):
        print("No solution exists")
    else:
        print_maze(sol)
        return False

def main_algo(maze,x,y,sol): # the main algo that performs the recursion we need the maze the current position the move 
    # ending the maze
    if x == n - 1 and y == n - 1 and maze[x][y]== 1: 
        sol[x][y] = 1
        return True
    # if the maze is valid 

    if is_safe(x,y,n)==True:
        # now we need to mark the solution path
        sol[x][y] = 1 # make it one 
        # move to the next cell 
        # update x and y also
        # moving in x is true
        if main_algo(maze,x+1,y,sol)==True:
            return True
        # x is not possible hence trying y 
        if main_algo(maze,x,y+1,sol)==True:
            return True
        
        # if none of them works then we have to backtrack and unmark the path
        sol[x][y]=0
        return False

if __name__ == "__main__": 
    # Initialising the maze 
    maze = [ [1, 0, 0, 0], 
             [1, 1, 0, 1], 
             [0, 1, 0, 0], 
             [1, 1, 1, 1] ] 
               
    algorithm(n,maze) 