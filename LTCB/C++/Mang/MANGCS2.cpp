#include <iostream>
using namespace std;

#define sn int
#define nhap cin
#define xuat cout
#define kt return 0

sn main(){
    sn a[100];
    sn n; // số lượng phần tử trong mảng
    sn x; // biến tạm để đọc dữ liệu từ bàn phím
    
    while(nhap >> x){ // đọc dữ liệu từ bàn phím cho đến khi không còn dữ liệu
        a[n] = x; // lưu giá trị x vào mảng a tại vị trí n
        n++; // tăng n lên 1 để chuẩn bị cho phần tử tiếp theo
    }
    for(sn i = 0; i < n; i++){
        xuat << a[i] << " ";
    }
}