#include <bits/stdc++.h>
using namespace std;
int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    ifstream fin("input.txt");
    ofstream fout("output.txt");
    long long a,b;
    if(fin>>a>>b) fout<<a+b;
    return 0;
}