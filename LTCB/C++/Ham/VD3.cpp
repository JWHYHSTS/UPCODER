// Liệt kê số thuần nguyên tố trong đoạn [1, N].
/*
Số thuần nguyên tố thỏa mãn : 

- N là số nguyên tố
- N có tất cả các chữ số là số nguyên tố
- N có tổng chữ số là số nguyên tố 
*/
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
sn csnt(sn n){
    while(n > 0){
        sn cs = n % 10;
        if(cs != 2 && cs != 3 && cs != 5 && cs != 7) 
        return 0;
        n /= 10;
    }
    return 1;
}

sn main(){
    sn n;
    nhap >> n;
    for(sn i = 1; i <= n; ++i){
        if(snt(i) && csnt(i) && tongcs(i)) xuat << i <<" ";
    }
    kt; 
}