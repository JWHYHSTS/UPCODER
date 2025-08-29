#include <bits/stdc++.h>
using namespace std;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    string s;
    if(!(cin >> s)) return 0;
    deque<char> q;
    string out;
    for(char c : s){
        if(c=='*'){
            if(!q.empty()){
                out.push_back(q.front());
                q.pop_front();
            }
        } else {
            q.push_back(c);
        }
    }
    cout << out;
    return 0;
}