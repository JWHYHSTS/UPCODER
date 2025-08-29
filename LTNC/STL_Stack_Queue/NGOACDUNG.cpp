#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    string s;
    if(!getline(cin, s)) return 0;
    stack<char> st;
    unordered_map<char,char> match = {{')','('}, {']','['}, {'}','{'}};
    for(char c : s){
        if(c=='('||c=='['||c=='{') st.push(c);
        else if(c==')'||c==']'||c=='}'){
            if(st.empty() || st.top()!=match[c]){
                cout<<"no";
                return 0;
            }
            st.pop();
        } else { 
            cout<<"no";
            return 0;
        }
    }
    cout<<(st.empty() ? "yes" : "no");
    return 0;
}