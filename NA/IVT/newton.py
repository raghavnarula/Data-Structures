import math

def new_function(x):
    return math.cos(x) - 0.5 - math.sin(x)

def derivative(x):
    return -math.sin(x) - math.cos(x)

x0 = 1
tol = 0.0001
x1 = 0
while abs(x0-x1) > tol:
    x1 = x0 - new_function(x0)/derivative(x0)
    print(x1)
    x0 = x1


