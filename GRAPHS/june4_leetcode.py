import collections
deadends = ["0201","0101","0102","1212","2002"]
dead_set = set(deadends)

queue = collections.deque([('0000',0)])
visited = set('0000') # string to set
print(queue)
print(visited)

while queue:
    string,steps = queue.popleft()
    print(string,steps)
    if string == target:
        return steps
    elif string in dead_set:
        continue
        
    for i in range(4):
        digit = int(string[i])
        for move in [-1, 1]:
            new_digit = (digit + move) % 10
            new_string = string[:i]+str(new_digit)+string[i+1:]
            if new_string not in visited:
                visited.add(new_string)
                queue.append((new_string, steps+1))