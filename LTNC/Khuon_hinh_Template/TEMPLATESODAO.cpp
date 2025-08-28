#include <bits/stdc++.h>
using namespace std;
long long reverseAbs(long long n){
    n = llabs(n);
    long long r=0;
    while(n){
        r = r*10 + n%10;
        n/=10;
    }
    return r;
}
int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    string line;
    long long sumInt=0,sumSD=0;
    bool haveInt=false,haveSD=false;
    long long maxInt=0;
    long long maxSDVal=0;
    long long maxSDOrig=0;
    while (getline(cin,line)){
        if(line.empty()) continue;
        stringstream ss(line);
        string t; long long n;
        if(!(ss>>t>>n)) continue;
        if(t=="T"){
            sumInt+=n;
            if(!haveInt || n>maxInt) maxInt=n;
            haveInt=true;
        }else if(t=="D"){
            long long rev = reverseAbs(n);
            sumSD+=rev;
            if(!haveSD || rev>maxSDVal){
                maxSDVal=rev;
                maxSDOrig=n;
            }
            haveSD=true;
        }
    }
    if(haveInt) cout<<sumInt<<"\n"; else cout<<"khong co\n";
    if(haveInt) cout<<maxInt<<"\n"; else cout<<"khong co\n";
    if(haveSD) cout<<sumSD<<"\n"; else cout<<"khong co\n";
    if(haveSD) cout<<"[SoDao] "<<maxSDOrig<<"\n"; else cout<<"khong co\n";
    return 0;
}