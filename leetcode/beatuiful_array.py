def beautifulArray(N):
        res = [1]
        while len(res) < N:
            res = [i * 2 - 1 for i in res] + [i * 2 for i in res]
            print(res)
        return [i for i in res if i <= N]

print(beautifulArray(4))