# printing all the palindromic partitions

import time
t = time.time()
def checker(string,s,e):
    # print(f'checking on {string}')
    if e<=s:
        return True
    else:
        # check if start == end
        if string[s] != string[e]:
            return False
        checker(str(string),s+1,e-1)
    return True

list1 = []
list2 = []

s = 'aabac'
list_s = list(s)

def partition(string,start,end):
    for i in range(start,end):
        l = []
        for j in range(i):
            l.append(string[j])
            print(string[j],end=" ")
        l.sort()
        l = "".join(l)
        if checker(l,0,len(l)-1) == True:
            list2.append(l)
        print()
for i in range(len(list_s)):
    a = list_s[i:]
    partition(a,1,len(a)+1)

# print(f"final list is {list2}")
a = list(set(list2))
a.sort()
print(a)
e = time.time()
# print(e-t)