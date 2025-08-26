#include <iostream>
using namespace std;

#define sn int
#define nhap cin
#define xuat cout
#define kt return 0

sn ucln(sn a, sn b){
    a = abs(a);
    b = abs(b);
    while (b != 0){
        sn t = a % b;
        a = b;
        b = t;
    }
    return a;
}
sn bcnn(sn a, sn b){
    return (a*b) / ucln(a,b);
}

sn main(){
    sn a,b;
    nhap >> a >> b;
    xuat << ucln(a,b) <<" " << bcnn(a,b);
    kt;
}