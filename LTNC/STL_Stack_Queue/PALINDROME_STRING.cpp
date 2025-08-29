#include <bits/stdc++.h>
using namespace std;

struct Stack {
    vector<char> a;
    void push(char c){ a.push_back(c); }
    char pop(){ char c=a.back(); a.pop_back(); return c; }
    bool empty() const { return a.empty(); }
};

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    string all,line;
    while(true){
        string tmp;
        if(!getline(cin,tmp)) break;
        all += tmp;
    }
    if(all.empty()) return 0;
    Stack st;
    vector<char> t;
    for(char c: all){
        if(isalnum((unsigned char)c)){
            char lc = tolower((unsigned char)c);
            t.push_back(lc);
            st.push(lc);
        }
    }
    vector<char> rev; rev.reserve(t.size());
    while(!st.empty()) rev.push_back(st.pop());
    cout << (t==rev ? "YES" : "NO");
    return 0;
}