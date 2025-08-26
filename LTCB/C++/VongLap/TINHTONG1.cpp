#include <iostream>
#include <cmath>
#include <iomanip>
using namespace std;

#define sn int
#define st double
#define nhap cin
#define xuat cout
#define kt return 0

sn main(){
    sn n;
    nhap >> n;
    st tong = 0;
    for(sn i = 1; i <= n; i++){
        tong += 1.0/ pow(i,3);
    }
    xuat << fixed << setprecision(3) << tong; 
}