#include <iostream>
#include <cmath>
using namespace std;

#define sn int
#define nhap cin
#define xuat cout
#define kt return 0

bool snt(sn n){
    if(n < 2 ) return false;
    for(int i = 2; i <= sqrt(n); i++){
        if(n % i == 0) return false;
    }
    return true; 
}
sn main(){
    sn n;
    nhap >> n;
    if(snt(n)) xuat << "YES";
    else xuat << "NO"; 
    kt;
}