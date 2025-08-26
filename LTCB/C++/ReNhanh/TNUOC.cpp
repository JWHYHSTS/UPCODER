#include <iostream>
#include <cmath>
using namespace std;

#define nt int
#define nhap cin
#define xuat cout
#define kt return 0 

nt main(){
    nt n;
    nhap >> n;
    nt st = 0;
    if(n == 16 ) xuat << st*7000;
    else if(n >=17 && n <= 50) xuat << 16*7000 + (n-16)*8500;
    else if(n > 51) xuat << 16*7000 + 34*8500 + (n-50)*100000;
    kt;
}