#include <bits/stdc++.h>
using namespace std;

vector<long long> L; // lengths

char solve(long long n, int k){
    if(k == 0){
        return (n == 1) ? 'b' : 'o';
    }
    long long left = L[k-1];
    long long mid_len = k + 3; // "b" + (k+2) 'o'
    if(n <= left) return solve(n, k-1);
    if(n <= left + mid_len){
        return (n - left == 1) ? 'b' : 'o';
    }
    return solve(n - left - mid_len, k-1);
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int T;
    if(!(cin >> T)) return 0;
    vector<long long> qs(T);
    long long maxN = 0;
    for(int i=0;i<T;i++){ cin >> qs[i]; maxN = max(maxN, qs[i]); }
    L.push_back(3); // L0
    int k=0;
    while(L.back() < maxN){
        ++k;
        L.push_back(2*L.back() + (k + 3));
    }
    int maxk = (int)L.size()-1;
    for(long long n: qs){
        cout << solve(n, maxk) << "\n";
    }
    return 0;
}