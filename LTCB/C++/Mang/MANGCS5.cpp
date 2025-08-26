#include <iostream>
#include <cmath>
using namespace std;

#define sn int
#define nhap cin
#define xuat cout
#define kt return 0

sn scp(sn x){
    if(x < 0) return 0;
    sn cbh_x = sqrt(x);
    return (cbh_x * cbh_x == x);
}
sn main(){
    sn a[100];
    sn n;
    sn x;
    while(nhap >> x){
        a[n] = x;
        n++;
    }
    sn tong = 0;
    for(sn i = 0; i < n; i++){
        if(scp(a[i])){
            tong += a[i];
        }
    }
    xuat << tong;
    kt;
    
}