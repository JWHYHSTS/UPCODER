// Tìm ước chung lớn nhất của 2 số a và b
#include <iostream>
using namespace std;

#define sn int
#define nhap cin
#define xuat cout
#define kt return 0 

sn main(){
    sn a, b;
    nhap >> a >> b;
    sn min = (a<b) ? a:b; // Tìm số nhỏ hơn giữa a và b
    for( sn i = min; i >= 1; i--){ // Duyệt từ min đến 1
        if((a%i == 0) && (b%i == 0)){ // Kiểm tra nếu i là ước chung
            xuat << i <<" ";
            break;
        }
    }
}