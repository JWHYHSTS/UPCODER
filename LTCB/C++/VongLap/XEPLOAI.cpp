#include <iostream>
#include <cmath>
#include <iomanip>
using namespace std;

#define sn int
#define st double
#define nhap cin
#define xuat cout
#define kt return 0

sn main(){
    sn diem, tong = 0, dem = 0;
    while(nhap >> diem && diem != -1){
        tong += diem;
        dem++;
    }
    if(dem == 0){
        xuat <<"F";
    }
    st dtb = static_cast<st>(tong) / dem;
    if(dtb < 4) xuat << "F"; 
    else if(4<= dtb && dtb < 5.5) xuat << "D";
    else if(5.5 <=dtb && dtb < 7) xuat << "C";
    else if(7 <= dtb && dtb < 8.5) xuat << "B";
    else xuat <<"A";
    kt;
}