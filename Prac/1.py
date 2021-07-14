## Subsets using backtracking

# [1,2,3] = [1] [2] [3] [1,2] [1,3] [1,2,3] [2,3]

# repeat nhi hona chahiye number

d = []
subset = []
def backtraking(arr,subset,start):
    
    d.append(subset.copy())
    # print(*subset)
    for i in range(start,len(arr)):
        if arr[i] == arr[i-1]:
            continue
        subset.append(arr[i])
        backtraking(arr,subset,i+1)
        # print("I am popping",subset[-1])
        subset.pop()
        # print("subset now: ",subset)
    return

a = [1,2,2]
a.sort()
backtraking(a,[],0)

print(d)


