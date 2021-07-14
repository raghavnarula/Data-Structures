## matrix element to rotate

def rotate(mat,target):
    N = len(mat[0])
    count = 0
    while count!=4:
        for i in range(N // 2):
            for j in range(i, N - i - 1):
                temp = mat[i][j]
                mat[i][j] = mat[N - 1 - j][i]
                mat[N - 1 - j][i] = mat[N - 1 - i][N - 1 - j]
                mat[N - 1 - i][N - 1 - j] = mat[j][N - 1 - i]
                mat[j][N - 1 - i] = temp
        
        if mat == target :
            return True    
        count += 1
    return False
        


mat = [[0,0,0],[0,1,0],[1,1,1]]
target = [[1,1,1],[0,1,0],[0,0,0]]


print(rotate(mat,target))  