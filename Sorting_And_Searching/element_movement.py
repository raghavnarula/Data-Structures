a = [1,2,3,4,5,6,7,8,9]
# make 7 move to the position 3
for i in range(len(a)):
    temp = a[6]

for i in range(3,len(a)-1):
    temp = a[i+1]
    a[i+1] = a[i]
    a[i]
print(a)