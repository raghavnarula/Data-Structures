def binary(arr,find,start,end):
    
    while start <= end:
    
        mid = (start + end) // 2
        
        
        if arr[mid] == find:
            return True
        
        if find < arr[mid]:
            end = mid-1
            
        if find > arr[mid] :
            start = mid+1
            
        print("index:",mid)

binary([i for i in range(32)],31,0,31)