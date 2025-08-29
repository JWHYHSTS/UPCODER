#include <bits/stdc++.h>
using namespace std;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n;
    if(!(cin >> n)) return 0;
    vector<long long> v(n);
    for(int i=0;i<n;++i) cin >> v[i];
    string rest;
    getline(cin, rest); 
    string line;
    if(!getline(cin, line)) line="";
    stringstream ss(line);
    vector<long long> cmd;
    long long x;
    while(ss >> x) cmd.push_back(x);

    if(cmd.size()==1){
        long long pos = cmd[0];
        if(pos == -1){
            v.clear();
        }else if(0 <= pos && pos < (long long)v.size()){
            v.erase(v.begin() + pos);
        }
    }else if(cmd.size()>=2){
        long long a = cmd[0], b = cmd[1];
        if(a < 0) a = 0;
        if(b > (long long)v.size()) b = v.size();
        if(a < b){
            v.erase(v.begin()+a, v.begin()+b);
        }
    }

    if(v.empty()){
        cout << "empty";
    }else{
        for(size_t i=0;i<v.size();++i){
            if(i) cout << ' ';
            cout << v[i];
        }
    }
    return 0;
}