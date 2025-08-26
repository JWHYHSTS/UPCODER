#include <iostream>
using namespace std;

#define sn int
#define nhap cin
#define xuat cout
#define kt return 0

sn main(){
    sn n;
    nhap >> n;
    for(sn i = 1; i <= n; i++){
        for(sn j = 1; j < 2*n; j++){
            if(j >= i && j <= 2*n - i) xuat <<"*";
            else xuat <<" ";
        }
        if(i < n) xuat << endl;
    }
    kt;
}