#include <iostream>
using namespace std;
#define nt int
#define nhap cin
#define xuat cout
#define kt return 0
#define va &&

int main(){
    nt n;
    nhap >> n;
    if(n % 3 == 0 va n % 7 != 0){
        xuat << 1;
    }else{
        xuat << 0;
    }
    kt; 
}