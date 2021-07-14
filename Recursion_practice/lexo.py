def final(cur,end):
    if cur > end:
        return
    print(cur)
    
    for i in range(10):
        new_cur = 10*cur + i 
        # print(new_cur)
        if new_cur > end:
            return 
        final(new_cur,end)
        
# final(1,12)
def printer(n):
    for i in range(1,10):
        final(i,n)    
        
printer(11)