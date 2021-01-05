a = [1,3,5,7,9,24]
b = [2,4,6,8,10,11]
final = []
# merge these arrays
i = j = 0
while i <len(a) and j < len(b):
    # compare the elements one by one
    # print(i,j)
    print(a[i],b[i])
    if a[i] < b[j]:
        final.append(a[i])
        i = i+1
    elif a[i]>b[j]: # element of b is smaller
        final.append(b[j])
        j = j + 1
    else:
        # equal element found
        final.append(a[i])
        final.append(b[j])

# check if any elemnt is left in the array 
for x in range(i,len(a)):
    final.append(a[x])
for x in range(j,len(b)):
    final.append(b[x])
