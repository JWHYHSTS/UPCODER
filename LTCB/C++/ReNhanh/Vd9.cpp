#include <iostream>
#include <cmath>
using namespace std;
#define nt int
#define nhap cin
#define xuat cout
#define kt return 0
#define va &&
#define hoac ||

int main(){
    nt a,b,c;
    nhap >> a >> b >>c;
    if(a == b va b == c){
        xuat << 1;
    }else if(a == b hoac a == c hoac b == c){
        xuat << 2;
    }else if(a == sqrt(b*b + c*c) hoac b == sqrt(a*a + c*c) hoac c == sqrt(a*a + b*b)){
        xuat << 3;
    } else {
        xuat << 4; 
    }
    kt; 
}