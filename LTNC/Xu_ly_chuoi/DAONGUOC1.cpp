#include <bits/stdc++.h>
using namespace std;

long long rev_num(long long x){
    long long r = 0;
    while(x){
        r = r*10 + x%10;
        x /= 10;
    }
    return r;
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    long long v;
    long long bestOrig = -1, bestRev = -1;
    while(cin >> v){
        long long rv = rev_num(v);
        if(rv > bestRev){
            bestRev = rv;
            bestOrig = v;
        }
    }
    if(bestOrig != -1) cout << bestOrig;
    return 0;
}