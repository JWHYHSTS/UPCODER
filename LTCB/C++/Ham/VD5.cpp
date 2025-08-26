// Số Thuận Nghịch
#include <iostream>
#include <cmath>
using namespace std;

#define sn int
#define nhap cin
#define xuat cout 
#define kt return 0 

sn stn(sn n){
    sn m = 0, tmp = n;
    while(tmp > 0){
        m = m * 10 + tmp % 10;
        tmp /= 10;
    }
    if(m == n) return 1;
    return 0;
}

sn main(){
    sn n;
    while(nhap >> n){
    if(stn(n)) xuat << "YES" << endl;
    else xuat << "NO"; 
    }
    kt;
}