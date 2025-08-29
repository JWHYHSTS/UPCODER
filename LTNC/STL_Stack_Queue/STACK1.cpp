#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    string s;
    if(!(cin >> s)) return 0;
    vector<char> st;
    string out;
    for(char c : s){
        if(c=='*'){
            if(!st.empty()){
                out.push_back(st.back());
                st.pop_back();
            }
        } else {
            st.push_back(c);
        }
    }
    cout << out;
    return 0;
}