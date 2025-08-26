#include <iostream>
using namespace std;

#define sn int
#define ll long long
#define nhap cin
#define xuat cout
#define kt return 0

sn main(){
    ll n;
    nhap >> n;
    ll kq = -1;
    ll p = 1;
    while(n / p >= 10) p *= 10;
    ll m = n;
    while(p > 0){
        ll l = n / (p*10);
        ll r = n % p;
        ll f = l * p + r;
        if(f > kq) kq = f;
        p/=10;
    }
    xuat << kq;
    kt;
}