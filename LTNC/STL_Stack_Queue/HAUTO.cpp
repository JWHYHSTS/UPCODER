#include <bits/stdc++.h>
using namespace std;

struct Stack {
    int cap;
    long long *a;
    int sz;
};

void init(Stack &st, int capacity) {
    st.cap = capacity;
    st.a = new long long[capacity];
    st.sz = 0;
}

bool full(Stack &st) { return st.sz == st.cap; }
bool empty(Stack &st) { return st.sz == 0; }

void push(Stack &st, long long x) {
    if(full(st)) return;
    st.a[st.sz++] = x;
}

long long top(Stack &st) {
    return st.a[st.sz-1];
}

long long pop(Stack &st) {
    if(empty(st)) return 0;
    return st.a[--st.sz];
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    string line;
    if(!getline(cin, line)) return 0;
    stringstream ss(line);
    vector<string> tokens;
    string tk;
    while(ss >> tk) tokens.push_back(tk);
    if(tokens.empty()) return 0;
    Stack st;
    init(st, (int)tokens.size());
    for(const string &t : tokens){
        if(t=="+" || t=="-" || t=="*"){
            long long b = pop(st);
            long long a = pop(st);
            if(t=="+") push(st, a + b);
            else if(t=="-") push(st, a - b);
            else push(st, a * b);
        } else {
            push(st, stoll(t));
        }
    }
    cout << top(st);
    delete[] st.a;
    return 0;
}