// Bộ 3 số Pytago
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
    bool ktra = false;
    for(sn i = 1; i <= n; i++){
        for(sn j = i; j <= n; j++){
            sn k2 = i*i + j*j;
            sn k = sqrt(k2);
            if(k*k == k2 && k <= n){
                xuat << i <<" " << j << " "<< k << endl;
                ktra = true;
            }
        }
    }
    if(!ktra) xuat << -1; 
    kt;
}