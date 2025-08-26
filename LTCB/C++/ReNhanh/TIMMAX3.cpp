#include <iostream>
#include <algorithm>
using namespace std;

#define nt int
#define nhap cin
#define xuat cout
#define kt return 0 

nt main(){
    nt a,b,c,d,e;
    nhap >> a >> b >> c >> d >> e;
    // nt max1 = a;
    //if(b > max1) max1 = b;
    //if(c > max1) max1 = c;     
    //if(d > max1) max1 = d;
    //if(e > max1) max1 = e;
    nt max1 = max({a,b,c,d,e});
    xuat << max1;
    kt; 
}