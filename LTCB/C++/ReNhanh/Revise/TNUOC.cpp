/*
Công ty cấp nước Nam Định lắp đặt cho mỗi hộ gia đình trong tỉnh 1 công tơ và quy định bảng giá tính tiền nước theo chỉ số công tơ cho từng tháng sau:
16 số đầu thì tính 7.000đ/số
Từ số 17 đến số 50 thì tính 8.500đ/số
Từ số 51 trở lên thì tính 100.000đ/số
Yêu cầu: Em hãy lập trình tính số tiền nước của 1 hộ gia đình phải trả theo bảng giá trên
Ví dụ:

Input
20
Output
146000
*/
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
    nt st = 0;
    if(n == 16 ) xuat << st*7000;
    else if(n >=17 && n <= 50) xuat << 16*7000 + (n-16)*8500;
    else if(n > 51) xuat << 16*7000 + 34*8500 + (n-50)*100000;
    kt;
}