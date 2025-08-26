#include <iostream>
#include <cmath>
#include <iomanip>
using namespace std;

#define sn int
#define st double
#define nhap cin
#define xuat cout
#define kt return 0

// Hàm tính tổng các ước số của n ( bao gồm cả chính nó)
sn tonguoc(int n) {
    sn tong = 0;
    for (sn i = 1; i <= sqrt(n); i++) {
        if (n % i == 0) {
            tong += i;
            if (i != n / i) tong += n / i; // nếu i là ước số thì n/i cũng là ước số
        }
    }
    return tong;
}
// Hàm tính tổng các ước số của n ( không bao gồm chính nó)
int tonguoc_khong_chinh(int n) {
    int tong = 0;
    for (int i = 1; i <= sqrt(n); i++) {
        if (n % i == 0) {
            if (i != n) tong += i;
            int j = n / i;
            if (j != i && j != n) tong += j;
        }
    }
    return tong;
}

sn tichchuso(sn n){
    sn tich = 1, dem = 0; 
    while(n > 0){
        sn cs = n % 10;
        tich *= cs;
        n /= 10;
        dem++;
    }
    return tich; 
}
sn main(){
    sn n,m;
    nhap >> n >> m;
    if(n < 10) {xuat <<"NO";
    kt;
    }
    if( tichchuso(n)== tonguoc(m)) xuat << "YES";
    else xuat << "NO";
    kt;
}