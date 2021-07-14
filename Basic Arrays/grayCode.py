def grayCode(n):
    def final(n):
        if n==1:
            return [0,1]
        else:
            add = []
            for i in final(n-1)[::1]:
                string =""
                string += "0" + str(i)
                add.append(string)
            for i in final(n-1)[::-1]:
                # print(x)
                string = ""
                string += "1" + str(i)
                add.append(string)
        # add = binary_decimal(add)
        return add

    def binary_decimal(a):
        add = []
        for i in a:
            print(i)
            number = 0
            # print(i)
            add.append(int(i,2))
        return add
    return binary_decimal(final(n))
        
print(grayCode(3))
