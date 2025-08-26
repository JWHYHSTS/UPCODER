#include <iostream>
#include <cmath>
using namespace std;

#define sn int
#define nhap cin
#define xuat cout
#define kt return 0

sn snt(sn n){
    if(n < 2) return 0;
    for(sn i = 2; i <= sqrt(n); i++){
        if(n%i==0) return 0;
    }
    return 1;
}

sn main(){
    sn n;
    nhap >> n;
    sn a[n];
    sn tong = 0;
    for(sn i = 0; i < n; i++){
        nhap >> a[i];
    }
    for(sn i = 0; i < n; i++){
        if(snt(a[i])) {tong += a[i];}
    }
    xuat << tong;
    kt;
}