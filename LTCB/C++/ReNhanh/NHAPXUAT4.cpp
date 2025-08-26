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
    nt b = (n / 100)%10; 
    if( n > 100) xuat << b; 
    else xuat << -1; 
}