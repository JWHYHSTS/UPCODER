//Dãy Con Giống Nhau Dài Nhất
#include <iostream>
#include <cmath>
using namespace std;

#define sn int
#define nhap cin
#define xuat cout
#define kt return 0

sn main(){
    sn n;
    nhap >> n;
    sn a[n];
    for(sn i = 0; i < n; i++){
        nhap >> a[i];
    }
    sn dem = 1, kq = 1;
    for(sn i = 1; i < n; i++){
        if(a[i] == a[i-1]){
            dem++;
        }else{
            if(dem > kq){
                kq = dem;
            }
            dem = 1; // Reset dem khi gặp phần tử khác
        }
    }
    if(dem > kq){
        kq = dem; // Kiểm tra lần cuối nếu chuỗi cuối cùng là dài nhất
    }
    xuat << kq;
    kt;
}