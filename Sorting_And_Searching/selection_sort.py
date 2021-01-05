# finding the minimum element in the array repeatedly

a = [1,4,2,5,4,3,6,0,10]
print(a)

for j in range(len(a)-1):
# Now i want to make is the traversing this array again and again
# This gives me the minimum in the array  
    min = 9999999999999
    for i in range(j,len(a)):
        if a[i] < min:
            # update the minimum
            min = a[i]
            pos = i
        # swap the min now with the first element of the subarray
        # record the position of the min too 
    print(f"swapping {a[pos]} and {a[j]}")

    a[pos],a[j] = a[j],a[pos]
print(a)

