// Nhập vào 1 số nguyên từ bàn phím nếu nhập số âm thì yêu cầu nhập lại, nhập số không âm thì cho dừng
#include <iostream>
using namespace std;

#define sn int
#define nhap cin
#define xuat cout
#define kt return 0

sn main(){
    sn n;
    do{
        xuat << "nhap n: ";
        nhap >> n;
    }while (n < 0); // Yêu cầu nhập lại nếu n âm
    kt; 
}