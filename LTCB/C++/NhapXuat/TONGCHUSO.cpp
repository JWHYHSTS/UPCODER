#include <iostream>
#include <algorithm>
using namespace std;

#define sn int
#define ktu char
#define nhap cin
#define xuat cout
#define kt return 0

sn main(){
    sn a;
    nhap >> a;
    sn dv = a % 10;
    sn hc = a /10;
    xuat << dv + hc;
    kt;
}