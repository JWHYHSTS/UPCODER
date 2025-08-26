#include <iostream>
#include <cmath>
using namespace std;

#define sn int
#define ll long long
#define nhap cin
#define xuat cout
#define kt return 0

sn main(){
    for(sn a = 1; a <= 9 ; a++){
        sn c = a + 6;
        if(c > 9) continue;
        sn b = c - 3;
        if(b < 0 || b > 9) continue;
        sn sc = a * 100 + b * 10 + c;
        sn sm = a * 1000 + b * 100 + c;
        if(sm - sc == 2250){
            xuat << sc;
        } 
    }
    kt;
}