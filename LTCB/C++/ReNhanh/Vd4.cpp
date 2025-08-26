#include <iostream>
using namespace std;
#define nt int
#define nhap cin
#define xuat cout
#define kt return 0
#define va &&
#define hoac ||

int main(){
    nt n;
    nhap >> n;
    if(n % 3 == 0 hoac n % 7 == 0){
        xuat << 1;
    }else{
        xuat << 0;
    }
    kt; 
}