s = 'xyzzaz'
count = 0
for i in range(0,len(s)-2,1):
    substring = s[i]+s[i+1]+s[i+2]
    l = list(substring)
    set_ = set(l)
    if len(set_) == len(l):
        count += 1

return (count)