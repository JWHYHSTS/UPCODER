//Kiểm Tra Mảng Tăng Dần
#include <iostream>
#include <cmath>
using namespace std;

#define sn int
#define nhap cin
#define xuat cout
#define kt return 0

sn ktraMTD(sn a[], sn n){
    for(sn i = 1; i < n; i++){
        if(a[i] < a[i-1]) return 0;
    }
    return 1;
}

sn main(){
    sn n;
    nhap >> n;
    sn a[n];
    for(sn i = 0; i < n; i++){
        nhap >> a[i];
    }
    if(ktraMTD(a,n)) xuat << "Mang tang dan";
    else xuat << "Mang ko tang dan";
    kt;
}