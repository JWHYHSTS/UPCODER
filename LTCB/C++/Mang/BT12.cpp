// Dãy nguyên tố dài nhất
#include <iostream>
#include <cmath>
using namespace std;

#define sn int
#define nhap cin
#define xuat cout
#define kt return 0

sn snt(sn n){
    if (n < 2) return 0;
    for(sn i = 2; i <= sqrt(n); i++){
        if(n%i == 0) return 0;
    }
    return 1;
}

sn main(){
    sn n;
    nhap >> n;
    sn a[n]; 
    for(sn i = 0; i < n; i++){
        nhap >> a[i];
    }
    sn dem = 0, tong = 0;
    sn res_dem = 0, res_tong = 0, batdau = -1;

    for(sn i = 0; i < n; i++){
        if(snt(a[i])){
            dem++;
            tong += a[i];
        }else{
            if(dem > res_dem){
                res_dem = dem;
                res_tong = tong;
                batdau = i - res_dem; // Lưu chỉ số bắt đầu của dãy con nguyên tố dài nhất
            }
            else if(dem == res_dem){
                if(tong > res_tong){
                    res_tong = tong;
                    batdau = i - res_dem;
                }
            }
        dem = 0; 
        tong = 0; // Reset đếm và tổng khi gặp phần tử không phải nguyên tố
        }
    }
    if(dem > res_dem){
        res_dem = dem;
        res_tong = tong;
        batdau = n - res_dem;
    }
    else if(dem == res_dem){
        if(tong > res_tong){
            res_tong = tong;
            batdau = n - res_dem;
        }
    }
    if(batdau == -1) xuat <<"Mang ko chua so nguyen to";
    else{
        for(sn i = 0; i < res_dem; i++){
            xuat << a[batdau + i] <<" ";
        }
    }
    kt;
}