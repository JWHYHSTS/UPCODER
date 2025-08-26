// Đếm và liệt kê các số thuận nghịch trong mảng
#include <iostream>
#include <cmath>
using namespace std;

#define sn int
#define nhap cin
#define xuat cout
#define kt return 0

sn thuannghich(sn n){
    sn bd = 0, tmp = n;
    while(n != 0 ){
        bd = bd * 10 + n % 10;
        n /= 10;
    }
    return bd == tmp;
}

sn main(){
    sn n;
    nhap >> n;
    sn a[n];
    for(sn i = 0; i < n; i++){
        nhap >> a[i];
    }
    sn dem = 0;
    for(sn i = 0; i < n; i++){
        if(thuannghich(a[i])){
            xuat << a[i] <<" ";
            dem++;
        }
    }
    xuat << endl;
    xuat << dem;
    kt;
}