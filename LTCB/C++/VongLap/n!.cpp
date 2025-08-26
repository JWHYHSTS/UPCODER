#include <iostream>
using namespace std;

#define sn int
#define nhap cin
#define xuat cout
#define kt return 0

sn main(){
    sn n, gt = 1;
    nhap >> n;
    for(sn i = 1; i <= n; i++){
        gt *= i;
    }
    xuat << gt;
    kt;
}