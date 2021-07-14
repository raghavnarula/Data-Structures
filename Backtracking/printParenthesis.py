# we have to print all the paranthesis in balanced form ...

res = []
def para_helper(n,string,open,closed,pos):
    
    
    # ending condtion
    
    if closed == n:
        
        
        print(string)
        res.append("".join(string))
        return 

    else:
        # close != n here we have 2 cases...
        
        if open < n :
            string[pos] = "(" # add a (
            
            para_helper(n,string,open+1,closed,pos+1)
        if open > closed: # add a )
            string[pos] = ")"
            
            para_helper(n,string,open,closed+1,pos+1)

n = 3
string = [""] * 2 * n # this is the maximum possible string size 
if n > 0:
    pos = 0
    open = 0
    closed = 0
    para_helper(n,string,open,closed,pos)
    
    
print(res)