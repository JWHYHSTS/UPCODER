// TÍNH TỔNG CHỮ SỐ CỦA N
#include <iostream>
using namespace std;

#define nt int
#define nhap cin
#define xuat cout
#define kt return 0

nt main(){
    int n;
    nhap >> n;
    int sum = 0;
    while ( n != 0){
        sum += n %10; // Lấy chữ số cuối cùng
        n /= 10; // Loại bỏ chữ số cuối cùng
    }
    xuat << sum;
    kt;
}