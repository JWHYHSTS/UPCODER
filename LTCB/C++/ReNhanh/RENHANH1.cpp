#include <iostream>
using namespace std;

#define nt int
#define nhap cin
#define xuat cout
#define va &&
#define kt return 0

nt main(){
    nt n;
    nhap >> n;
    if(n % 3 == 0) {
        xuat << n <<"chia het cho 3";
    } else if(n % 3 == 1) {
        xuat << n << "chia 3 du 1";
    } else xuat << n << "chia 3 du 2"; 
    kt; 
}