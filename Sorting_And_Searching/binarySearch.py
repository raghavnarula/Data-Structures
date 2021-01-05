a = [1,2,3,4,5,6,7]
first = 0
last = len(a) - 1

element = int(input("element: "))
flag = 0
while first < last:
    mid = ( first + last ) / 2
    # compare the mid with the element
    if mid == element:
        flag = 1
        print(f"The element is found")
        break
    elif mid > element:
        # update the last 
        last = mid
    elif mid < element:
        first = mid
    else:
        print("element not found")

if flag == 0:
    print("element not found")    