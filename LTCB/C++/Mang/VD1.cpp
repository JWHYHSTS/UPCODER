#include <iostream>
using namespace std;

#define sn int
#define nhap cin
#define xuat cout
#define kt return 0

void nhapmang(sn a[],sn n){
    for(sn i = 0; i < n; i++){
        nhap >> a[i];
    }
}

void xuatmang(sn a[], sn n){
    for(sn i = 0; i < n; i++){
        xuat << a[i] << " ";
    }
}

sn main(){
    sn n;
    nhap >> n;
    sn a[n];
    nhapmang(a,n);
    xuatmang(a,n);
    kt;
}