#include <bits/stdc++.h>
using namespace std;

string to_hex(unsigned long long n){
    const string digits="0123456789ABCDEF";
    if(n < 16) return string(1, digits[n]);
    return to_hex(n/16) + digits[n%16];
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    unsigned long long n;
    if(!(cin>>n)) return 0;
    cout << to_hex(n);
    return 0;
}