// Hình chữ nhật sao rỗng
#include <iostream>
using namespace std;

#define sn int
#define nhap cin
#define xuat cout
#define kt return 0

sn main(){
    sn a,b;
    nhap >> a >> b;
    for(sn i = 1; i <= a; i++){
        for(sn j = 1; j <= b; j++){
            if(i == 1 || i == a || j == 1 || j == b){
                xuat <<"*";
            } else xuat <<" ";
        }
        if(i < a) xuat << endl;
    }
    kt;
}