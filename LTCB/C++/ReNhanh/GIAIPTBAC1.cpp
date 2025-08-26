#include <iostream>
#include <cmath>
#include <iomanip>
using namespace std;

#define nt int
#define st double
#define nhap cin
#define xuat cout
#define kt return 0 
#define va &&

nt main(){
    st a,b;
    nhap >> a >> b;
    if (a == 0 va b == 0) xuat << "VSN";
    if (a == 0 va b != 0) xuat <<"VN";
    if( a != 0 ) xuat <<fixed << setprecision(2) << -b / a;
    kt; 
}