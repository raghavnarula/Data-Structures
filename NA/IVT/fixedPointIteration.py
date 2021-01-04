import math

def function(x):
    return math.sqrt(10/(4+x))

# find one root of the equation approximataly

x0 = 10000000
tolerance = 0.0001
temp = 0 # x1 x2 so onnn....
for i in range(10):
    # x1 = phi(x0)
    temp = function(x0)
    x0 = temp 
    temp = round(temp,4)
    print(temp) 
    # error comparison between the a and b 


# x + x**2 -10 = 0
# x = (10 - x**2) == g(x)
# x = (sqrt(10-x)) == g(x)
# 

x1 = x0 - f(x0)/f'(x0)