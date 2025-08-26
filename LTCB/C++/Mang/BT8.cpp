//Dãy Con Cỡ K có Tổng Lớn Nhất
#include <iostream>
#include <cmath>
using namespace std;

#define sn int
#define nhap cin
#define xuat cout
#define kt return 0

sn main(){
    sn n, k;
    nhap >> n >> k;
    sn a[n];
    for(sn i = 0; i < n; i++){
        nhap >> a[i];
    }
    
    for(sn i = 0; i <= n - k; i++){
        sn tong = 0;
        for(sn j = 0; j < k; j++){
            tong += a[i + j];
        }
        xuat << "Tong day con bat dau tu chi so " << i << " la: "<<tong<<endl;
    }
    kt;
}