## here we are going to make basic heaps..
import math
a = [10,20,15,30,40]

# make a complete binary tree for it..

# first find  it's parent
# parent = set()
# for i in range(1,len(a)):
#     print(int((i-1)/2))
#     parent.add(a[int((i-1)/2)])

# print(parent)

# now we know the parents now we to find their child's

for i in range(len(a)):

    try:
        print(f"children of {a[i]} are {a[2*i+1]} and {a[(2*i)+2]}")
        # print(f"right child of {a[i]} is {a[(2*i)+1]}")
    except IndexError:
        print(f"None for {a[i]}")


# Create max heap..

# only th root 
a = [10]
