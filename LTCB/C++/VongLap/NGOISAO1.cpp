#include <iostream>
using namespace std;

#define sn int
#define nhap cin
#define xuat cout
#define kt return 0

sn main(){
    sn n;
    while(nhap >> n){
        for(sn i = 1; i <= n; i++){
            for(sn j = 1; j <= i; j++){
                xuat <<"*"; 
            }
            xuat << endl;
        }   
    }
    kt;
}