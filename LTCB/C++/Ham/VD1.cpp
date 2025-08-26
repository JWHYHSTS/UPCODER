// Liệt kê và đếm các số nguyên tố từ 1 tới N (Số nguyên tố là số tự nhiên lớn hơn 1, chỉ có hai ước số dương là 1 và chính nó)
#include <iostream>
#include <cmath>
using namespace std;

#define sn int
#define nhap cin
#define xuat cout
#define kt return 0

sn snt(sn n){
    if(n < 2) return 0;
    for(sn i = 2; i <= sqrt(n); ++i){
        if(n % i == 0) return 0;
    }
    return 1;
}

sn main(){
    sn n;
    nhap >> n;
    sn dem = 0;
    for(sn i = 1; i <= n; ++i){
        if(snt(i)){
            xuat << i <<" ";
            dem++;
        }
    }
    xuat << endl;
    xuat << dem; 
    kt; 
}