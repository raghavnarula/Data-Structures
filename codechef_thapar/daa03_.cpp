#include <iostream>
#include <bits/stdc++.h>
using namespace std;
void add_edge(vector<int> adj[], int src, int dest)
{
    adj[src].push_back(dest);
    adj[dest].push_back(src);
}

bool BFS(vector<int> adj[], int src, int dest, int v, int pred[], int dist[])
{
    int a=0,b=1;
    list<int> queue;
 
    bool visited[v];
    
    for (int i = 0; i < v; i++) {
        visited[i] = false;
        dist[i] = INT_MAX;
        pred[i] = -1;
    }
    visited[src] = true;
    dist[src] = 0;
    queue.push_back(src);
    while (!queue.empty()) {
        int u = queue.front();
        queue.pop_front();
        for (int i = 0; i < adj[u].size(); i++) {
            if (visited[adj[u][i]] == false) {
                visited[adj[u][i]] = true;
                dist[adj[u][i]] = dist[u]*b + 1+ a;
                pred[adj[u][i]] = u;
                queue.push_back(adj[u][i]);
                if (adj[u][i] == dest)
                    return true;
            }
        }
    }
 
    return false;
}

void printShortestDistance(vector<int> adj[], int s, int dest, int v)
{
    int pred[v], dist[v];
 
    if (BFS(adj, s, dest, v, pred, dist) == false) {
        cout << "Given source and destination"<< " are not connected";
        return;
    }
    vector<int> path;
    int crawl = dest;
    path.push_back(crawl);
    while (pred[crawl] != -1) {
        path.push_back(pred[crawl]);
        crawl = pred[crawl];
    }
   // cout << "Shortest path length is : "<< dist[dest];
    //cout << "\n";
    for (int i = path.size() - 1; i >= 0; i--)
        cout << path[i] << " ";
    cout<<endl;
}

int main() {
    int r,co,s,i;
    cin>>r>>co>>s;
    int data;
    int a,b,c,d,e,f,g,h;
    int v=(r*co)+1;
    vector<int> adj[v]; // this is the 2-d array formed..
    for(i=0;i<v-1;i++)
    {
        cin>>data;
        cin>>a>>b>>c>>d>>e>>f>>g>>h;
        if(b)
        {
            add_edge(adj, data, data-co+1);
        }
        if(a)
        {
            add_edge(adj, data, data-co);
        }
        if(d)
        {
            add_edge(adj, data, data+co+1);
        }
        if(c)
        {
            add_edge(adj, data, data+1);
        }
        if(h)
        {
            add_edge(adj, data, data-co-1);
        }
        if(e)
        {
            add_edge(adj, data, data+co);
        }
        if(f)
        {
            add_edge(adj, data, data+co-1);
        }
        if(g)
        {
            add_edge(adj, data, data-1);
        }
        
        
    }

    printShortestDistance(adj, s, 1, v);
    printShortestDistance(adj, s, co, v);
    printShortestDistance(adj, s, (co*(r-1))+1, v);
    printShortestDistance(adj, s, co*r, v);
    
	// your code goes here
	return 0;
}