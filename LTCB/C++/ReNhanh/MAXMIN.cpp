#include <iostream>
#include <bits/stdc++.h>
using namespace std;

#define nt int
#define nhap cin
#define xuat cout
#define ktu char
#define kt return 0

nt main(){
    nt n;
    nhap >> n;
    nt hn = n / 1000;
    nt tr = (n/100) % 10;
    nt ch = (n/10) % 10;
    nt dv = n % 10;
    /*nt max1 = hn;
    if(tr > max1) max1 = tr;
    if(ch > max1) max1 = ch;
    if(dv > max1) max1 = dv;
    nt min1 = hn;
    if(tr < min1) min1 = tr;
    if(ch < min1) min1 = ch;
    if(dv < min1) min1 = dv;
    xuat << max1 + min1;*/
    nt max1 = max({hn,tr,ch,dv});
    nt min1 = min({hn,tr,ch,dv});
    xuat << max1 + min1;
    kt;
    
}