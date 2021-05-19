def binary(a,low,high,key):
    ## Ending condition of the recursion -> 
    # if we have the last element in the array 
    print("Final->",low," ",high)
    if low == high:
        if a[low] == key:
            return low 
        else:
            return 0  
    else:
        # low != high
        mid = int((low + high)//2)

        if key == a[mid]:
            return mid
        elif key < a[mid]:
            # left side
            return binary(a,low,mid-1,key)
        else:
            # go for the right side
            return binary(a,mid+1,high,key)

if __name__ == "__main__":
    arr = [1,2,3,4,5,6,7,8,9,10]
    print (binary(arr,0,len(arr)-1,110))

