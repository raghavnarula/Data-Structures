def ReversespiralPrint(m, n, a): 
  
    # Large array to initialize it 
    # with elements of matrix 
    b = [0 for i in range(100)] 
  
    i = 0   
    #/* k - starting row index 
    #l - starting column index*/ 
    k = 0
    l = 0
    # print(a[1][1])
    # Counter for single dimension array 
    # in which elements will be stored 
    z = 0
  
    # Total elements in matrix 
    size = m * n 
  
    while (k < m and l < n): 
          
        # Variable to store value of matrix. 
        val = 0
  
        # Print the first row  
        # from the remaining rows  
        for i in range(l, n): 
              
            # printf("%d ", a[k][i]) 
            val = a[k][i] 
            b[z] = val 
            z += 1
        k += 1
  
        # Print the last column 
        # from the remaining columns 
        for i in range(k, m): 
  
            # printf("%d ", a[i][n-1]) 
            val = a[i][n - 1] 
            b[z] = val 
            z += 1
  
        n -= 1
  
        # Print the last row  
        # from the remaining rows 
        if (k < m): 
            for i in range(n - 1, l - 1, -1): 
                  
                # printf("%d ", a[m-1][i]) 
                val = a[m - 1][i] 
                b[z] = val 
                z += 1
  
        m -= 1
  
        # Print the first column  
        # from the remaining columns  
        if (l < n): 
            for i in range(m - 1, k - 1, -1): 
                  
                # printf("%d ", a[i][l]) 
                val = a[i][l] 
                b[z] = val 
                z += 1
            l += 1
  
    for i in range(size - 1, -1, -1): 
        print(b[i], end = " ") 
  
# Driver Code 


# number = int(input())                                

# list_num = list(map(int, input().split(' ')[:3]))
# a = list_num[2] # number of non zero enteries

# rows, cols = list_num[0],list_num[1]
# my_matrix = [([0]*cols) for i in range(rows)]


# for i in range(a):
#     list_num = list(map(int, input().split(' ')[:3]))
#     # row _index col_index value
#     my_matrix[list_num[0]][list_num[1]] = list_num[2]

# print(my_matrix,end =" ")

a = [[8,0,0,0], 
     [0,6,5,0], 
     [0,0,0,9],
     [0,0,7,0]] 

ReversespiralPrint(3, 3, a) 
# rows and columns and the matrix as input