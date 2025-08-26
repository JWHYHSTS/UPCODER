#include <iostream>
#include <cmath>
using namespace std;

#define nt int
#define nhap cin
#define xuat cout
#define kt return 0 

nt cp(nt n){
    if(n < 0 ) return 0;
    int a = sqrt(n);
    if(a*a == n) return 1; 
    return 0;
}

nt main(){
    nt n;
    nhap >> n;
    if(cp(n)){
        xuat<<"yes";
    }else xuat<<"no";
    kt; 
}