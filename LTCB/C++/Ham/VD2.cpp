// Liệt kê các số có tổng chữ số là số nguyên tố trong đoạn [1, N]
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
sn tongcs(sn n){
    sn tong = 0;
    while(n > 0){
        tong += n %10;
        n /= 10;
    }
    return snt(tong); 
}

sn main(){
    sn n;
    nhap >> n;
    for(sn i = 1; i <= n; ++i){
        if(tongcs(i) == 1) xuat << i << " ";
    }
    kt; 
}