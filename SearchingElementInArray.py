# we are given a sorted 2d array and we have to find an element in it
'''
we are using divide and conquer algortihm to do this

1) finding the middle element in the array.
[
[1,2,3] 
[4,5,6]               start_row + (end_row - start_row)//2 --> rows and columns both..
[7,8,9]                
]
that is 5 --> now we see that number(k) is greater or smaller than the middle 
element..

Case 1: k=6 greater
search the matrix on the lower side of the element
that is -> [7,8,9] (again use the same technique)
and also the matrix on the right side of the middle element -> 
that is-[
	[2,3]
	[5,6]  
	]
now again find the middle element --> start_row = 1 and end = 2 
				      start_column = 0 end = 1
middle = i(for row) = 1 + (2-1)//2  == 1 
	j(for column) = 0 + (1-0)//2 == 0 
	middle element is (0,1) --> 3
	again greater or less

Now if the element is less ->> 
we have to search for the vertical left matrix and the top right matrix

that is for example 
	[
	[1,2,3] 
	[4,5,6]               
	[7,8,9]
	]
search  [
	1
	4
	7
	]
	and 
	[2,3]
	[5,6] 



ending condition 
--> element mached or the 
start of the row == end of the row or
start of the column == end of the column
'''

def search(mat, fromRow, toRow, fromCol, toCol, key): 

	# Find middle and compare with middle 
	i = fromRow + (toRow - fromRow) // 2
	j = fromCol + (toCol - fromCol) // 2 
	if (mat[i][j] == key): # If key is present at middle 
		print("Found " , key , " at " , i , " " , j)
		return 
	else: 

		# right-up quarter of matrix is searched in all cases. 

		# Provided it is different from current call 
		if (i != toRow or j != fromCol): 
			search(mat, fromRow, i, j, toCol, key)

		# Special case for iteration with 1*2 matrix 
		# mat[i][j] and mat[i][j+1] are only two elements. 
		# So just check second element 
		if (fromRow == toRow and fromCol + 1 == toCol): 
			if (mat[fromRow][toCol] == key): 
				print("Found " , key , " at " , fromRow , " " , toCol)
				return
		# If middle key is lesser then search lower horizontal 
		# matrix and right hand side matrix 
		if (mat[i][j] < key): 

			# search lower horizontal if such matrix exists 
			if (i + 1 <= toRow): 
				search(mat, i + 1, toRow, fromCol, toCol, key)

		# If middle key is greater then search left vertical 
		# matrix and right hand side matrix 
		else: 
			
			# search left vertical if such matrix exists 
			if (j - 1 >= fromCol): 
				search(mat, fromRow, toRow, fromCol, j - 1, key)

# Driver code 
if __name__ == '__main__': 
	mat = [[ 10, 20, 30, 40], 
		[15, 25, 35, 45], 
		[27, 29, 37, 48], 
		[32, 33, 39, 50]]
	rowcount = 4; colCount = 4; key = 50

	for i in range(rowcount): 
		for j in range(colCount): 
			search(mat, 0, rowcount - 1, 0, colCount - 1, mat[i][j])





