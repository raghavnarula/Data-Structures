def reverse_spiral():
    current_direction = 0
    previous_direction = 0
    current_column = start_col
    current_row = start_row
 
    counter = 1
 
    while 1:
        for _ in range(2):
            for _ in range(counter):
                if matrix[current_row][current_column]:
                    print(current_row, current_column, matrix[current_row][current_column], previous_direction + 1)
                previous_direction = current_direction
 
                if current_direction == 0:
                    current_row += 1
                    if current_row >= rows:
                        return
                elif current_direction == 1:
                    current_column += 1
                    if current_column >= columns:
                        return
                elif current_direction == 2:
                    current_row -= 1
                    if current_row < 0:
                        return
                elif current_direction == 3:
                    current_column -= 1
                    if current_column < 0:
                        return
                else:
                    pass
 
            current_direction = (current_direction + 1) % 4
        counter += 1
 
 
if __name__ == '__main__':
    rows, columns, sparse_size = [int(x) for x in input().strip().split()]
 
    matrix = [[0 for _ in range(columns)] for _ in range(rows)]
    matrix[0][0] = 5
    for i in range(sparse_size):
        a = input().strip().split()
        matrix[int(a[0])][int(a[1])] = int(a[2])
 
    start_row, start_col = [int(x) for x in input().strip().split()]
 
    reverse_spiral()