// Chèn thêm phần tử vào mảng
#include <iostream>
#include <cmath>
using namespace std;

#define sn int
#define nhap cin
#define xuat cout
#define kt return 0

sn main(){
    sn n, k, x;
    nhap >> n >> k >> x;
    sn a[n];
    for(sn i = 0; i < n; i++){
        nhap >> a[i];
    }

    for(sn i = n - 1; i >= k; i--){ // Dịch các phần tử về bên phải để tạo chỗ trống
        a[i+1] = a[i]; // Dịch các phần tử về bên phải (vd i = 3 thì a[4] = a[3] -> a[4] = gtri cua a[3], a[5] = a[4] -> a[5] = gtri cua a[4], ... )
    }
    a[k] = x; // Chèn phần tử x vào vị trí k
    n++;
    xuat <<"Mang sau khi chen: ";
    for(sn i = 0; i < n; i++){
        xuat << a[i] << " ";
    }
    kt;
}