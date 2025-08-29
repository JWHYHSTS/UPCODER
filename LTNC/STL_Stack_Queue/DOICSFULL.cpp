#include <bits/stdc++.h>
using namespace std;

struct Stack {
    int cap;
    int sz;
    vector<char> a;
    void init(int c=32){ cap=c; sz=0; a.assign(cap, 0); }
    bool full(){ return sz==cap; }
    bool empty(){ return sz==0; }
    void push(char x){
        if(full()){
            cap *= 2;
            a.resize(cap);
        }
        a[sz++] = x;
    }
    char top(){ return a[sz-1]; }
    char pop(){ return a[--sz]; }
};

string chuyenCoSo(long long soHe10, int heCoSoMoi=0){
    int base = (heCoSoMoi==0 ? 2 : (heCoSoMoi==1 ? 8 : 16));
    if(soHe10 == 0) return "0";
    const string digits = "0123456789ABCDEF";
    Stack st; st.init();
    long long n = soHe10;
    while(n > 0){
        st.push(digits[n % base]);
        n /= base;
    }
    string res;
    while(!st.empty()) res.push_back(st.pop());
    return res;
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    vector<string> lines;
    string line;
    while(true){
        if(!getline(cin, line)) break;
        if(line.find_first_not_of(" \t\r\n") == string::npos) continue;
        lines.push_back(line);
    }
    bool first = true;
    for(auto &ln : lines){
        stringstream ss(ln);
        long long val;
        int baseCode = 0;
        ss >> val;
        ss >> baseCode; 
        string out = chuyenCoSo(val, baseCode);
        if(!first) cout << "\n";
        first = false;
        cout << out;
    }
    return 0;
}
