// Số hoàn hảo (Eculid) tối ưa hơn
#include <iostream>
#include <cmath>
using namespace std;

#define sn int
#define ll long long
#define nhap cin 
#define xuat cout 
#define kt return 0

sn snt(sn n){
    if(n < 2) return 0;
    for(sn i = 2; i <= sqrt(n); i++){
        if(n % i == 0) return 0;
    }
    return 1;
}

sn shh(ll n){
    for(sn p = 2; p <= 33; p++){ // p bắt đầu từ 2
        if(snt(p)){
            ll tmp = pow(2, p) - 1;
            if(snt(tmp)){
                ll perfect = pow(2, p-1) * tmp;
                if(perfect == n) return 1;
            }
        }
    }
    return 0;
}

sn main(){
    ll n;
    nhap >> n;
    for(ll i = 1; i <= n; i++){
        if(shh(i)) xuat << i << " "; 
    }
    kt;
}