#include <iostream>
#include <cmath>
using namespace std;

#define sn int
#define nhap cin 
#define xuat cout
#define kt return 0

sn UCLN(sn a, sn b){
    while(b != 0){
        sn temp = a % b;
        a = b;
        b = temp;
    }
    return a;
}
sn BCNN(sn a, sn b){
    return a * b / UCLN(a,b);
}

sn main(){
    sn a,b;
    nhap >> a >> b;
    //xuat << UCLN(a,b);
    xuat << BCNN(a,b);
    kt;
}