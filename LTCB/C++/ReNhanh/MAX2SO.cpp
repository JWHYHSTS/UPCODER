#include <iostream>
#include <cmath>
#include <algorithm>
using namespace std;

#define nt int
#define nhap cin
#define xuat cout
#define kt return 0 

nt main(){
    nt a,b;
    nhap >> a >> b;
    if ( a > b ) xuat << a;
    else xuat << b; 
    kt;
}