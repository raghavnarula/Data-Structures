# Two pointers is really an easy and effective technique which is typically used for searching pairs in a sorted array.

list=[10,20,30,40,50] # the array must be sorted

sum_find = 70
# make 2 pointers one starting from start and one from end
i = 0
j = len(list)-1


# compare the elements
import sys
while i<j:
    sum_obtained = list[i] + list[j]
    if sum_obtained > sum_find:
        j = j-1
    elif sum_obtained < sum_find:
        i = i+1
    elif sum_obtained==sum_find: # we have found the pair
        print("we have found a pair!")
        sys.exit()

print("Not found")


########### Some questions on 2 pointer


