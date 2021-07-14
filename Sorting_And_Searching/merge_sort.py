a = [15,5,24,1,3,16,20,10]

# divide the aay into 2 halves
# print(len(a)//2)
def mergeSort(a):
    # divide the array into 1-1 subarrays
    if len(a)>1:
        half = len(a)//2
        left = a[:half]
        right = a[half:]
        print(left,right)
        mergeSort(left)
        mergeSort(right)
        # print("Print the list",a)

    # See merging the code for 2 sorted_arrays in the main folder for this 
        i = j = k = 0

        # Copy data to temp arrays left[] and right[]
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                a[k] = left[i]
                i += 1
            else:
                a[k] = right[j]
                j += 1
            k += 1

        # Checking if any element was left
        while i < len(left):
            a[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            a[k] = right[j]
            j += 1
            k += 1

mergeSort(a)
print(a)

