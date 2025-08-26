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
    if(n > 0) xuat << "DUONG";
    else if (n < 0) xuat <<"AM";
    else xuat << "KHONG"; 
}