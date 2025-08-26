#include <iostream>
using namespace std;

#define sn int
#define nhap cin
#define xuat cout
#define kt return 0

sn amstrong(sn n){
    sn tong = 0, m = n, dem = 0;
    while(m > 0){
        m /= 10;
        dem++;
    }
    m = n;
    while(m > 0){
        sn cs = m % 10;
        sn pow = 1;
        for(sn i = 0; i < dem; i++){
            pow *= cs;
        }
        m /= 10;
        tong += pow;
    }
    return tong;
}
sn main(){
    sn n;
    while(nhap >> n){
        if (amstrong(n) == n) xuat << "YES" << endl;
        else xuat << "NO" << endl;
    }
    kt;
}
/*
#include <iostream>
using namespace std;

#define sn int
#define nhap cin
#define xuat cout
#define kt return 0

sn pow_table[10][8]; // pow_table[d][k] = d^k, k từ 1 đến 7

void init_pow_table() {
    for(sn d = 0; d <= 9; d++)
        for(sn k = 1; k <= 7; k++) {
            sn p = 1;
            for(sn i = 0; i < k; i++) p *= d;
            pow_table[d][k] = p;
        }
}

bool amstrong(sn n){
    sn tong = 0, m = n, dem = 0;
    if(n == 0) dem = 1;
    else {
        while(m > 0){
            m /= 10;
            dem++;
        }
    }
    m = n;
    if(n == 0) tong = 0;
    else {
        while(m > 0){
            sn cs = m % 10;
            tong += pow_table[cs][dem];
            m /= 10;
        }
    }
    if(n == 0) return (tong == n);
    return (tong == n);
}

sn main(){
    sn n;
    init_pow_table();
    while(nhap >> n){
        if (amstrong(n)) xuat << "YES" << endl;
        else xuat << "NO" << endl;
    }
    kt;
}*/