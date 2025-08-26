#include <iostream>
#include <cmath>
using namespace std;
#define nt int
#define nhap cin
#define xuat cout
#define kt return 0
#define va &&
#define hoac ||

bool snt(nt n){
    if( n < 2) return false;
    for(nt i = 2; i <= sqrt(n); i++){
        if(n % i == 0) return false;
    } return true; 
}
int main(){
    nt n;
    nhap >> n;
    nt r = n%10; // lấy chữ số cuối

    if(n < 100 va snt(r)){
        xuat << 1;
    }else {
        xuat << 0; 
    }
    kt; 
}