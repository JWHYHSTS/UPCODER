#include <bits/stdc++.h>
using namespace std;

struct Stack {
    vector<string> a;
    void push(const string &s){ a.push_back(s); }
    string pop(){ string v=a.back(); a.pop_back(); return v; }
    string &top(){ return a.back(); }
    bool empty(){ return a.empty(); }
};

int prec(const string &op){
    if(op=="+"||op=="-") return 1;
    if(op=="*"||op=="/") return 2;
    if(op=="^") return 3;
    return 0;
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    string line, all;
    while(true){
        string tmp;
        if(!getline(cin,tmp)) break;
        if(!all.empty()) all.push_back(' ');
        all += tmp;
    }
    if(all.empty()) return 0;
    for(char &c: all) if(c=='\u2013') c='-';
    stringstream ss(all);
    vector<string> tokens;
    string tk;
    while(ss>>tk) tokens.push_back(tk);

    Stack st;
    vector<string> out;
    for(auto &t: tokens){
        if(!t.empty() && all_of(t.begin(), t.end(), ::isdigit)){
            out.push_back(t);
        } else if(t=="("){
            st.push(t);
        } else if(t==")"){
            while(!st.empty() && st.top()!="("){
                out.push_back(st.pop());
            }
            if(!st.empty() && st.top()=="(") st.pop();
        } else { 
            while(!st.empty() && st.top()!="("){
                string &tt = st.top();
                int pt=prec(tt), pc=prec(t);
                if(pt>pc || (pt==pc && t!="^")){
                    out.push_back(st.pop());
                } else break;
            }
            st.push(t);
        }
    }
    while(!st.empty()) out.push_back(st.pop());
    for(size_t i=0;i<out.size();++i){
        if(i) cout<<' ';
        cout<<out[i];
    }
    return 0;
}