#include <bits/stdc++.h>
using namespace std;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int N;
    if(!(cin>>N)) return 0;
    vector<long long> dp(N+1,0);
    dp[0]=1;
    for(int x=1;x<=N;++x){
        for(int s=N;s>=x;--s){
            dp[s]+=dp[s-x];
        }
    }
    long long ans = dp[N]-1; 
    if(ans<0) ans=0;
    cout<<ans;
    return 0;
}