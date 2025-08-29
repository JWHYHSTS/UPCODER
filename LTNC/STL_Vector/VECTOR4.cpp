#include <bits/stdc++.h>
using namespace std;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int N,Q;
    if(!(cin>>N>>Q)) return 0;
    vector<int> v(N);
    for(int i=0;i<N;++i) cin>>v[i];
    while(Q--){
        int t; cin>>t;
        if(t==1){
            int x,y; cin>>x>>y;
            if(x < 0) x = 0;
            if(x > (int)v.size()) v.push_back(y);
            else v.insert(v.begin()+x, y);
        }else if(t==2){
            int x; cin>>x;
            v.erase(remove(v.begin(), v.end(), x), v.end());
        }else if(t==3){
            int x; cin>>x;
            if(0 <= x && x < (int)v.size()) cout<<v[x]<<"\n";
            else cout<<"ERROR\n";
        }
    }
    return 0;
}