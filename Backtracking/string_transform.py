res = []
# subset = []
alphabet = 0
numbers_list = [i for i in range(10)]


def backtrack(sub="", i=0):
    if len(sub) == len(S):
        res.append(sub)
    else:
        if S[i].isalpha():
            backtrack(sub + S[i].swapcase(), i + 1)
            print(sub)
        backtrack(sub + S[i], i + 1)
        
                

S = "a1b2"
backtrack("",0)
print(list(res))
        