#include <iostream>
#include <cmath>
using namespace std;

#define sn int
#define nhap cin
#define xuat cout
#define kt return 0

sn main(){
    sn n;
    nhap >> n; 
    sn a[1000];
    for(sn i = 0; i < n; i++){
        nhap >> a[i];
    }
    for(sn i = 0; i < n; i++){
        xuat << a[i] << " ";
    }
    kt;
}