#include <iostream>
#include <cmath>
using namespace std;

#define sn int
#define ll long long
#define nhap cin
#define xuat cout
#define kt return 0

sn main(){
    ll n;
    nhap >> n;
    ll delta = 1 + 8 * n;
    ll sq = sqrt(delta);
    if(sq * sq != delta){
        xuat <<"NO";
        return 0;
    } 
    ll k = (-1 + sq) / 2;
    if(k > 0 && k * (k+1) / 2 == n){
        xuat <<"YES";
    }
    else xuat << "NO";
    kt;
}
