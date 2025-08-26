// Thao tác xóa phần tử trong mảng
#include <iostream>
#include <cmath>
using namespace std;

#define sn int
#define nhap cin
#define xuat cout
#define kt return 0

sn main(){
    sn n,k;
    nhap >> n >> k;
    sn a[n];
    for(sn i = 0; i < n; i++){
        nhap >> a[i];
    }

    for(sn i = k; i < n; i++){
        a[i] = a[i+1]; // Dịch các phần tử về bên trái vd: i = 3 thì a[3] = a[4] thì a[3] sẽ nhận giá trị của a[4], a[4] = a[5] -> a[4] sẽ nhận giá trị của a[5], ...
    }
    n--; // Giảm kích thước mảng sau khi xóa
    xuat <<"Mang sau khi xoa: ";
    for(sn i = 0; i < n; i++){
        xuat << a[i] << " ";
    }
    kt;
}

