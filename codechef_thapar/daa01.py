'''
75 3 5
15 50 35
11 1
13 1
6 1
27 1
18 1
'''
'''
75 3 5
15 50 35
6 3
11 1
13 4
27 1
18 2
'''
import time
s = time.time()

basic_info = list(map(int, input().strip().split(' ')))
student_marks = list(map(int, input().strip().split(' ')))

subpart_main = []
marks = []

for i in range(basic_info[2]):
    a = tuple(map(int, input().strip().split(' ')))
    subpart_main.append(a[1])
    marks.append(a[0])

for student in student_marks:

    sum_marks = student
    subpart = subpart_main.copy()
    final = []

    while 1:
        if sum_marks >= basic_info[0]:
            break 
        value = max(subpart)
        # print(value)
        indices = [i for i, x in enumerate(subpart) if x == value]
        min_marks = 99999
        if len(indices) > 1:
            # update the min_marks
            for i in indices:
                if marks[i] < min_marks:
                    min_marks = marks[i]
            
            # make the min marks index
            sum_marks += min_marks
            delete_index = marks.index(min_marks)
            final.append(delete_index+1)
            subpart[delete_index] = -1

        else:
            # we have only 1 indice .. and 
            sum_marks += marks[indices[0]]
            final.append(indices[0]+1)
            subpart[indices[0]] = -1

    # print(final)\
    final.sort()
    print(len(final),end=" ")
    for i in final:
        print(i,end=" ")
    print()

e = time.time()
print(e-s)
