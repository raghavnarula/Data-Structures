a = [1,2,3,4,5]
final = [0 for i in range( len(a))]

for i in range(len(a)):
    final[(i+2)%(len(a))] = a[i] 
print(*final)    
    