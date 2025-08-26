#include <iostream>
#include <algorithm>
using namespace std;

#define sn int
#define ktu char
#define nhap cin
#define xuat cout
#define kt return 0

sn main(){
    sn a, b;
    nhap >> a >> b;
    swap(a, b);
    xuat << a << " " << b;
    kt;
}