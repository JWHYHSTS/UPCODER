#include <iostream>
using namespace std;

#define nt int
#define nhap cin
#define xuat cout
#define kt return 0

nt main(){
    int a, b, tong = 0;
    nhap >> a >> b;
    for (int i = a; i <= b; i++){
        if(i % 3 == 0){
            tong += i;
            xuat << i <<" ";
        }
    }
    xuat << endl;
    xuat << tong;
    kt;
}