#include <bits/stdc++.h>
using namespace std;

struct Stack {
    int cap, sz;
    vector<char> a;
    void init(int c){ cap=c; sz=0; a.assign(cap, 0); }
    bool full(){ return sz==cap; }
    bool empty(){ return sz==0; }
    void push(char x){
        if(full()){ cap*=2; a.resize(cap); }
        a[sz++] = x;
    }
    char top(){ return a[sz-1]; }
    char pop(){ return a[--sz]; }
};

int prec(char op){
    if(op=='+'||op=='-') return 1;
    if(op=='*'||op=='/') return 2;
    if(op=='^') return 3;
    return 0;
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    string s, line;
    while(true){
        string tmp;
        if(!getline(cin,tmp)) break;
        s += tmp;
    }
    if(s.empty()) return 0;
    s.erase(remove_if(s.begin(), s.end(), ::isspace), s.end());
    Stack st; st.init((int)s.size()+5);
    vector<string> out;
    for(char c: s){
        if(isdigit((unsigned char)c)){
            out.push_back(string(1,c));
        } else if(c=='('){
            st.push(c);
        } else if(c==')'){
            while(!st.empty() && st.top()!='('){
                out.push_back(string(1, st.pop()));
            }
            if(!st.empty() && st.top()=='(') st.pop();
        } else { // operator
            while(!st.empty() && st.top()!='('){
                char t = st.top();
                int pt = prec(t), pc = prec(c);
                if(pt > pc || (pt==pc && c!='^')){
                    out.push_back(string(1, st.pop()));
                } else break;
            }
            st.push(c);
        }
    }
    while(!st.empty()) out.push_back(string(1, st.pop()));
    for(size_t i=0;i<out.size();++i){
        if(i) cout << ' ';
        cout << out[i];
    }
    return 0;
}