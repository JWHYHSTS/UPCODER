// UCLN, BCNN 
#include <iostream>
#include <cmath>
using namespace std;

#define sn int
#define nhap cin
#define xuat cout
#define kt return 0

sn ucln(sn a, sn b){
    while(b != 0){
        sn tmp = a % b;
        a = b;
        b = tmp;
    }
    return a;
}
sn bcnn(sn a, sn b){
    return a * b / ucln(a,b);
}

sn main(){
    sn a,b;
    nhap >> a >> b;
    xuat << ucln(a,b) << " " << bcnn(a,b);
    kt;
}