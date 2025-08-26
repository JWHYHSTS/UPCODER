#include <iostream>
using namespace std;

#define nt int
#define nhap cin
#define xuat cout
#define kt return 0

nt main(){
    int a,b,c,d;
    nhap >> a >> b >> c >> d;
    nt max1 = a;
    if(b > max1) max1 = b;
    if(c > max1) max1 = c;
    if(d > max1) max1 = d;
    nt max2 = -1e9;
    if(a > max2 && a < max1) max2 = a;
    if(b > max2 && b < max1) max2 = b;
    if(c > max2 && c < max1) max2 = c;
    if(d > max2 && d < max1) max2 = d;
    if(max2 == -999999) cout <<"-1";
    else cout << max2;
    kt;
}