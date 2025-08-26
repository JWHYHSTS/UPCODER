#include <iostream>
using namespace std;
#define nt int
#define nhap cin 
#define xuat cout 
#define kt return 0 
#define va &&
#define hoac ||

int main(){
    nt t, m;
    nhap >> t >> m; 
    switch (t){
        case 1: case 3: case 5: case 7: case 8: case 10: case 12:
        xuat << 31;
        break;
        case 4: case 6: case 9: case 11:
        xuat << 30; 
        break; 
        case 2:
        if( m % 400 == 0 hoac (m % 4 == 0 va m % 100 != 0)){
            xuat <<29; 
        }
        else xuat << 28; 
        break; 
        default: xuat << "ERROR"; 
    }
    kt; 
}