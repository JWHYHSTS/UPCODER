#include <iostream>
#include <cmath>
using namespace std;

#define nt int
#define nhap cin
#define xuat cout
#define kt return 0 

nt main(){
    nt n;
    nhap >> n;
    if(n% 2 == 0){
        xuat <<"chan";
    } else cout <<"le";
    kt; 
}