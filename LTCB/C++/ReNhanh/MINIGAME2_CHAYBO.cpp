#include <iostream>
using namespace std;

#define sn int
#define nhap cin
#define xuat cout
#define kt return 0

sn main(){
    sn a,b,c,tgian;
    nhap >> a >> b >> c >> tgian;
    sn res = a + b + c;
    res = tgian % res;
    
    if(res == 0 || res == a + b + c) xuat << "A";
    else if(res == a) xuat << "B";
    else if(res == a + b) xuat << "C";
    else if(res > 0 && res < a) xuat << "AB";
    else if(res > a && res < a + b) xuat <<"BC";
    else if(res > a + b && res < a + b + c) xuat << "CA";
    kt;
}