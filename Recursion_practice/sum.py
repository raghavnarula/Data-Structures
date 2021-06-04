def sum(number):
    if number==0:
        return 0
    else:
        return sum(number-1) + number

print(sum(5))