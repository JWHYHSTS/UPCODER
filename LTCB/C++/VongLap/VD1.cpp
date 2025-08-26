#include <iostream>
using namespace std;

#define nt int
#define nhap cin
#define xuat cout
#define kt return 0

nt main(){
    /*int n;
    nhap >> n;
    for(int i = 1; i <= n; ++i){
        xuat << i <<" ";
    }
    xuat <<endl;
    for(int i = n; i >= 0; --i){
        xuat << i <<" ";
    }
        */
    int n = 4;
    int i = 1;
    while ( i<= n){
        xuat << i <<" ";
        i++;
    }
    kt;
}