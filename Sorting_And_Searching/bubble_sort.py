# Implementing the bubble sort algo

a = [1,4,2,5,4,3,6,0,10]

value = input("ascending or descending (a/d) : ")

for j in range(len(a)-1):
        # compare the ith element with the i+1 th element
    for i in range(len(a)-1):
        if value == "a":
            if a[i] > a[i+1]: # ascending
            # swap both 
                a[i],a[i+1] = a[i+1],a[i]
        else:
            if a[i] < a[i+1]: # descending
            # swap both 
                a[i],a[i+1] = a[i+1],a[i]
print(a)

