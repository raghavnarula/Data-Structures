a  = [
    [18,4,16,8],
    [23,13,20,11],
    [28,24,26,25],
    [1,30,15,19]
]
a = [18, 4, 16, 8, 23, 13, 20, 11, 28, 24, 26, 25, 1, 30, 15, 19]
# a = [1,2,3,4]

start = 0
end = len(a)
alpha = []
def divide_conquer(start,end,a):
    # end case
    if len(a)<=2:
        return 
    half = len(a)//2
    left = a[:half]
    right = a[half:end]

    divide_conquer(start,half,left)
    divide_conquer(half+1,end,right)
    
    # print(left,right)
    # if len(left) == 2 and len(right) ==2 :
    left.sort()
    right.sort()

    alpha.append(left)
    alpha.append(right)

    # see the halves and merge them ..
divide_conquer(start,end,a)
    
print(alpha)
print(len(alpha))


    

