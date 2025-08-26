#include <iostream>
using namespace std;

#define nt int
#define nhap cin
#define xuat cout
#define kt return 0

nt main(){
    int n, gt = 1;
    nhap >> n;
    for(int i = 1; i <= n; i++){
        gt *= i;
    }
    xuat << gt;
    kt;
}