# final = []
# def dfs(cur,n):
#     global final
#     print(cur)
#     final.append(cur)
#     if cur > n:
#         return
#     for i in range(10):
#         if(10*cur+i>n):
#             return;
#         dfs(10*cur+i,n)

# for i in range(1,10):
#     dfs(i,20)

# print(*final)
from typing import List
def lexicalOrder(n: int) -> List[int]:
    global final
    final = []
    
    def dfs(cur,n):
        print(cur)
        # global final
        # final.append(cur)
        if cur > n:
            return
        for i in range(10):
            if(10*cur+i>n):
                return;
            dfs(10*cur+i,n)
        
    for i in range(1,10):
        dfs(i,n)
    
    return final

lexicalOrder(12)