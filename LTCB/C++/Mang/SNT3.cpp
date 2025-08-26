#include <iostream>
#include <cmath>
using namespace std;

#define sn int
#define nhap cin 
#define xuat cout 
#define kt return 0

sn snt(sn n){
    if(n < 2) return 0;
    for(sn i = 2; i <= sqrt(n); i++){
        if(n%i == 0) return 0;
    }
    return 1;
}

sn main(){
    sn a,b;
    nhap >> a >>b;
    for(sn i = a; i <= b; i++){
        if(snt(i)){
            xuat << i << endl;
        }
    }
    kt;
}