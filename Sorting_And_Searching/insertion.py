# insertion sort

a = [1,4,2,5,4,3,6,0,10]
print(a)

for i in range(1,len(a)):
    # compare the element with all the previous elements before it
    key = a[i]
    j = i-1
    while j>=0 and a[j] > key:
        print(j)
        if a[i] < a[j] :
            # move a[i] before a[j]  .. 
            a[j + 1] = a[j] 
            j = j - 1
        a[j+1] = key
print(a)
