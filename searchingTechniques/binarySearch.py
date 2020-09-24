list = [1,2,3,5,6,7,8,9]
# we need to do the binary search algprithm
end = len(list)
start = 0
mid = int((start+end)/2)
middle = (start +end)//2
search = 0
print(mid)

while start<=end:
    if search > list[mid]:
        start =mid+1
        end = len(list)
    elif search ==list[mid]:
        print("element exists")
        break
    elif search<list[mid]:
        end = mid-1
        start = 0
    mid = int((start +end)/2)
    print(mid)
if start>end:
    print("element does not exist")





