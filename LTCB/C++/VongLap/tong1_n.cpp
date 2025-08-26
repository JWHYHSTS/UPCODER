#include <iostream>
#include <cmath>
using namespace std;

#define sn int
#define ll long long
#define nhap cin
#define xuat cout
#define kt return 0

sn main(){
    sn n, tong = 0;
    nhap >> n;
    for(sn i = 1; i <= n; i++){
        tong += i;
    }
    xuat << tong;
}