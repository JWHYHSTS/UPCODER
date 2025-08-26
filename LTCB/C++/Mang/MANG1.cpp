#include <iostream>
using namespace std;

#define sn int
#define nhap cin 
#define xuat cout 
#define kt return 0

sn main(){
    sn n;
    nhap >> n;
    sn a[n];
    for(sn i = 0; i < n; i++){
        nhap >> a[i];
    }
    sn tong = 0;
    for(sn i = 0; i < n; i++){
        tong += a[i];
    }
    xuat << tong;
    kt;
}