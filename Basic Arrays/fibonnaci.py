# print fibonacci

def func(number):
    if number<=1:
        return number
    return func(number-1) + func(number-2)

print(func(6))