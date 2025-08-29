#include <bits/stdc++.h>
using namespace std;

struct Stack {
    vector<char> a;
    void push(char x){ a.push_back(x); }
    char pop(){ char x=a.back(); a.pop_back(); return x; }
    bool empty() const { return a.empty(); }
    char top() const { return a.back(); }
};

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    long long n;
    if(!(cin>>n)) return 0;
    if(n==0){
        cout<<0;
        return 0;
    }
    Stack st;
    while(n>0){
        st.push(char('0'+(n%2)));
        n/=2;
    }
    string res;
    while(!st.empty()) res.push_back(st.pop());
    cout<<res;
    return 0;
}