#include <bits/stdc++.h>
using namespace std;
int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    ifstream fin("FSTREAM.inp");
    ofstream fout("FSTREAM.out");
    long long n;
    if(!(fin>>n)){ return 0; }
    if(n < 0){ fout<<"NO"; return 0; }
    long long r = llround(floor(sqrt((long double)n)));
    while((r+1)*(r+1) <= n) ++r;
    while(r*r > n) --r;
    fout << (r*r==n ? "YES" : "NO");
    return 0;
}