import math
a = 5
b = 6

def function(x):
    return x**2 - 29

error = 0.001

while True:
    if abs(b-a) < error:
        break
# for i in range(20):
    c = (a + b)/2
    
    value = function(c)
    print(format(c,"0.4f"))
    if value < 0:
        #update a 
        a = c
    elif value > 0:
        #update b   
        b = c
    else:
        break
