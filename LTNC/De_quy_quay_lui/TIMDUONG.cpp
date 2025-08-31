#include <bits/stdc++.h>
using namespace std;
int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int nV,nE,S,T;
    if(!(cin>>nV>>nE>>S>>T)) return 0;
    vector<vector<int>> adj(nV+1);
    for(int i=0;i<nE;i++){
        int a,b; cin>>a>>b;
        adj[a].push_back(b);
        adj[b].push_back(a);
    }
    vector<int> dist(nV+1,-1);
    queue<int> q;
    dist[S]=0; q.push(S);
    while(!q.empty()){
        int u=q.front(); q.pop();
        if(u==T) break;
        for(int v: adj[u]) if(dist[v]==-1){
            dist[v]=dist[u]+1;
            q.push(v);
        }
    }
    cout<<dist[T];
    return 0;
}