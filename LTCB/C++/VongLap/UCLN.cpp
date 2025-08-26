#include <iostream>
using namespace std;

#define sn int
#define nhap cin
#define xuat cout
#define kt return 0

sn ucln(sn a, sn b){
    while (b != 0){
        sn r = a % b;
        a = b;
        b = r;
    }
    return a;
}
sn main(){
    sn a,b;
    nhap >> a >> b;
    xuat << ucln(a,b); 
    kt;
}