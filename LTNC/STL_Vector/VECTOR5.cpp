#include <bits/stdc++.h>
using namespace std;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n;
    if(!(cin >> n)) return 0;
    vector<long long> v(n);
    for(int i=0;i<n;++i) cin >> v[i];
    long double avg = accumulate(v.begin(), v.end(), 0LL) / (long double)n;
    vector<long long> greaterVals;
    for(long long x : v) if(x > avg) greaterVals.push_back(x);
    cout << greaterVals.size() << "\n";
    if(greaterVals.empty()){
        cout << -1;
    }else{
        for(size_t i=0;i<greaterVals.size();++i){
            if(i) cout << ' ';
            cout << greaterVals[i];
        }
    }
    return 0;
}