#include <bits/stdc++.h>
using namespace std;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    vector<long long> v;
    long long x;
    while (cin >> x) v.push_back(x);

    for (auto it = v.begin(); it != v.end(); ++it){
        if (it != v.begin()) cout << ' ';
        cout << *it;
    }
    cout << "\n";
    for (auto rit = v.rbegin(); rit != v.rend(); ++rit){
        if (rit != v.rbegin()) cout << ' ';
        cout << *rit;
    }
    return 0;
}