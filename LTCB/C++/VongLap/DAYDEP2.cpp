#include <iostream>
using namespace std;

#define sn int
#define nhap cin
#define xuat cout
#define kt return 0

sn main(){
    sn n, tongcs = 0;
    while (nhap >> n && n != 0){
        tongcs += n;
    }
    if(tongcs % 100 == 00 ) xuat << "DEP";
    else if(tongcs % 100 == 55) xuat <<"TRUNGBINH";
    else xuat << "XAU";
    kt;

}