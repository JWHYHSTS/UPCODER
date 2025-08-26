#include <iostream>
using namespace std;

#define sn int
#define ll long long
#define nhap cin
#define xuat cout
#define kt return 0

sn ucln(ll a, ll b){
    while(b != 0){
        ll r = a % b;
        a = b;
        b = r;
    }
    return a;
}

sn main(){
    ll a,b;
    nhap >> a >> b;
    xuat << ucln(a,b);
    kt;
}