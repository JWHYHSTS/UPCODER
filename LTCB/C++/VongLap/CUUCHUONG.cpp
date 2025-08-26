#include <iostream>
using namespace std;

#define sn int
#define nhap cin
#define xuat cout
#define kt return 0

sn main(){
    sn n;
    nhap >> n;
    for(sn i = 1; i <= 10; i++){
        xuat << n << "x"<< i << "=" << n * i << endl;
    }
    kt;
}