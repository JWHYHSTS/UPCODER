// Số hoàn hảo 
#include <iostream>
#include <cmath>
using namespace std;

#define sn int
#define nhap cin 
#define xuat cout 
#define kt return 0

sn shh(sn n){
    sn tong = 0;
    for(sn i = 1; i <= n/2; i++){
        if(n%i == 0){
            tong += i;
        }
    }
    if(tong == n) return 1;
    return 0;
}

sn main(){
    sn n;
    nhap >> n;
    sn dem = 0;
    for(sn i = 1; i <= n; i++){
        if(shh(i)){
            xuat << i <<" ";
            dem++;
        }
    }
    xuat << endl;
    xuat << dem;
    kt;
}