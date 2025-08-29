#include <bits/stdc++.h>
using namespace std;

struct Stack {
    vector<char> a;
    void push(char c){ a.push_back(c); }
    char top(){ return a.back(); }
    void pop(){ a.pop_back(); }
    bool empty(){ return a.empty(); }
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
    string s,line;
    while(true){
        string tmp;
        if(!getline(cin,tmp)) break;
        s+=tmp;
    }
    if(s.empty()) return 0;
    s.erase(remove_if(s.begin(), s.end(), ::isspace), s.end());
    Stack st;
    string out;
    for(char c: s){
        if(c>='a' && c<='z'){
            out.push_back(c);
        } else if(c=='('){
            st.push(c);
        } else if(c==')'){
            while(!st.empty() && st.top()!='('){
                out.push_back(st.top()); st.pop();
            }
            if(!st.empty() && st.top()=='(') st.pop();
        } else { // operator
            while(!st.empty() && st.top()!='('){
                char t=st.top();
                int pt=prec(t), pc=prec(c);
                if(pt>pc || (pt==pc && c!='^')){ 
                    out.push_back(t); st.pop();
                } else break;
            }
            st.push(c);
        }
    }
    while(!st.empty()){
        out.push_back(st.top()); st.pop();
    }
    cout<<out;
    return 0;
}