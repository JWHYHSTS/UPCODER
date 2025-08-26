#include <iostream>
#include <cmath>
#include <algorithm>
using namespace std;

#define nt int
#define nhap cin
#define xuat cout
#define kt return 0 

void c1(){
    int a,b,c;
    nhap  >> a >> b >> c; 
    int max_value = a;
    int min_value = a;
    if(b > max_value){
        max_value = b;
    }
    if(c > max_value){
        max_value = c;
    }
    if(b < min_value){
        min_value = b;
    }
    if(c < min_value){
        min_value = c;
    }
    xuat << max_value << " " << min_value;
}

void c2() {
    int a, b, c;
    nhap >> a >> b >> c;
    int lon_nhat = max({a, b, c});
    int nho_nhat = min({a, b, c});
    xuat << lon_nhat << " " << nho_nhat;
}
nt main(){
    c2();
    kt; 
}