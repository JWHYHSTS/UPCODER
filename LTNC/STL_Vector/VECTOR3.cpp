#include <bits/stdc++.h>
using namespace std;

bool isPerfectSquare(long long x){
    if(x < 0) return false;
    long long r = llround(floor(sqrt((long double)x)));
    while((r+1)*(r+1) <= x) ++r;
    while(r*r > x) --r;
    return r*r == x;
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    vector<long long> v;
    long long x;
    while(cin >> x) v.push_back(x);

    vector<long long> res;
    for(long long val : v){
        if(!isPerfectSquare(val) && val % 2 == 0)
            res.push_back(val);
    }
    sort(res.begin(), res.end());
    for(size_t i=0;i<res.size();++i){
        if(i) cout << ' ';
        cout << res[i];
    }
    return 0;
}