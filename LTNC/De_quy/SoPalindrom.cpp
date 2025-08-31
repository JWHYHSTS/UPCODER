#include <bits/stdc++.h>
using namespace std;

bool is_pal(long long x){
    string s = to_string(x);
    string t = s;
    reverse(t.begin(), t.end());
    return s == t;
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n;
    if(!(cin>>n)) return 0;
    vector<string> out;
    for(int i=0;i<n;i++){
        long long m; cin>>m;
        if(is_pal(m)) out.push_back(to_string(m));
    }
    for(size_t i=0;i<out.size();++i){
        if(i) cout<<' ';
        cout<<out[i];
    }
    return 0;
}