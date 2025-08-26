#include <iostream>
using namespace std;

#define sn int
#define nhap cin
#define xuat cout
#define kt return 0

sn tongcs(sn n){
    sn tong = 0;
    while(n > 0){
        tong += n % 10;
        n /= 10;
    }
    return tong;
}

sn csd(sn m){
    while (m >= 10) m /= 10;
    return m;
}
sn main(){
    sn n,m,k;
    nhap >> n >> m >> k;
    if(tongcs(n) + csd(m) == k) xuat << "Yes";
    else xuat << "No";
    kt;
}