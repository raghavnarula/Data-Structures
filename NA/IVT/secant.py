# using the secant method to find the root .

def function(x):
    return x**2 - 2

tol = 0.0001
x2 = 0 # temp value x2 x3 x4 so onn..
x1 = 2
x0 = 1
tol = 0.0001
while abs(x1-x0)>tol:
# for i in range(10):
    x2 = (x0*function(x1) - x1*function(x0))/(function(x1)-function(x0))
    print(x2)
    # update 
    x0 = x1 # 2
    x1 = x2 # 1.33 

# x2 = x0*f(x1) - x1*f(x0)
#       -----------------
        # f(x1) - f(x0)
