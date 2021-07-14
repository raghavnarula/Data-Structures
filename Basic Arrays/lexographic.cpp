#include<bits/stdc++.h>
using namespace std;
void dfs(int cur,int ending)
{   
    if (cur > ending) return;
    cout<<cur<<endl;
    for(int i=0;i<10;i++)
    {
        int new_num = 10*cur + i ;
        // cout << new_num<<endl;
        if (new_num>ending) return;
        dfs(new_num,ending);
    }
}
int main()
{
// dfs(1,20);
for(int i=1;i<10;i++)
{
dfs(i,20);
}
}