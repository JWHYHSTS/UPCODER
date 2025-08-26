#include <iostream>
#include <cmath>
using namespace std;

#define sn int
#define nhap cin
#define xuat cout
#define kt return 0

sn gcd(sn a,sn b){
    while(b!=0){
        sn temp = a % b;
        a = b;
        b = temp;
    }
    return a;
}

sn main(){
    sn n,m;
    nhap >> n >> m;
    if(gcd(n,m) == 1) xuat << "yes";
    else xuat << "no";
    kt;
}