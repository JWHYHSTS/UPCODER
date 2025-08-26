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
    if(n < 1000) xuat << -1;
    else xuat << (n/1000) %10; 
    kt;
}