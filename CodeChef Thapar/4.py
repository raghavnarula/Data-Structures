# create a sparse matrix

list_num = list(map(int, input().split(' ')[:3]))
print(list_num)
a = list_num[2] # number of non zero enteries

rows, cols = list_num[0],list_num[1]
my_matrix = [([0]*cols) for i in range(rows)]

print(my_matrix)

for i in range(a):
    list_num = list(map(int, input().split(' ')[:3]))
    # row _index col_index value
    my_matrix[list_num[0]][list_num[1]] = list_num[2]

print(my_matrix)