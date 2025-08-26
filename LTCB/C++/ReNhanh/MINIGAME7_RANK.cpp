#include <iostream>
using namespace std;

#define nhap cin
#define xuat cout
#define kt return 0
#define sn int

sn main(){
    sn VangVN, BacVN, DongVN, VangTL, BacTL, DongTL, key;
    nhap >> VangVN >> BacVN >> DongVN >> VangTL >> BacTL >> DongTL >> key;
    
    if(key == 1){
        sn sumVN = VangVN + BacVN + DongVN;
        sn sumTL = VangTL + BacTL + DongTL;
        if(sumVN > sumTL) xuat << "VN";
        else if(sumVN < sumTL) xuat << "TL";
        else xuat << "TIE";
    }
    if(key == 2){
        if(VangVN == VangTL && BacVN == BacTL && DongVN == DongTL) xuat <<"TIE";
        else if(VangVN > VangTL) xuat << "VN";
        else if(VangVN == VangTL && BacVN > BacTL) xuat << "VN";
        else if(VangVN == VangTL && BacVN == BacTL && DongVN > DongTL) xuat << "VN";
        else xuat << "TL";
    }
    kt;
}