# find the upper case letters in string

num = input()
n = list(num)
def checker(n,start,end):
    if start == end:
        return 
    print(start,start+2)
    print("".join(n)[start:start+2])
    checker(n,start+1,end)

checker(n,0,len(n))

