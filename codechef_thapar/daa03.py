import sys

def add_edge(adj,src,dest):
    adj[src].append(dest)
    adj[dest].append(src)


def BFS(adj,src,dest,v,pred,dist):
    queue = []

    visited = [0 for i in range(v)]

    for i in range(v):
        visited[i] = False
        dist[i] = sys.maxint
        pred[i] = -1

    visited[src] = True
    dist[src] = 0

    queue.append(src)

    while(queue!=None):

        u = queue.pop(0)
        for i in range(0,len(adj[u])):
            if visited[adj[u][i]] == False:
                visited[adj[u][i]] = True
                dist[adj[u][i]] = dist[u]*b + 1+ a
                pred[adj[u][i]] = u
                queue.append(adj[u][i])
                if (adj[u][i] == dest):
                    return True
    return False

def printShortestDistance(adj,s,dest,v):
    # pred[v] , dist[v]
    pred = [0 for i in range(v)]
    dist = [0 for i in range(v)]

    if (BFS(adj, s, dest, v, pred, dist) == False):
        print(f"The given source and destination are not connected!")
        return

    path = []
    crawl = dest
    path.append(crawl)
    # print("Path is : ",path)
    while pred[crawl]!=-1:
        path.append(pred[crawl])
        crawl = pred[crawl]

    for i in range(len(path)-1,-1,-1):
        print(path[i],end=" ")
    print()


## Taking input ..
basic_info = list(map(int, input().strip().split(' '))) # row column start..
r = basic_info[0]
co = basic_info[1]
s = basic_info[2]

v = (r*co) + 1
adj = [[] for i in range(v)]

for i in range(v-1):
    # input a row ... 
    # data = int(input())
    information = list(map(int,input().split(' ')))
    data = information[0]
    a = information[1]
    b = information[2]
    c = information[3]
    d = information[4]
    e = information[5]
    f = information[6]
    g = information[7]
    h = information[8]

    if(b):
        add_edge(adj, data, data-co+1);
        
    if(a):
        add_edge(adj, data, data-co);
    
    if(d):
        add_edge(adj, data, data+co+1);
    
    if(c):
        add_edge(adj, data, data+1);
    
    if(h):
        add_edge(adj, data, data-co-1);
    
    if(e):
        add_edge(adj, data, data+co);
    317:11:02
    if(f):
        add_edge(adj, data, data+co-1);
    
    if(g):
        add_edge(adj, data, data-1);
        
printShortestDistance(adj, s, 1, v);
printShortestDistance(adj, s, co, v);
printShortestDistance(adj, s, (co*(r-1))+1, v);
printShortestDistance(adj, s, co*r, v);


