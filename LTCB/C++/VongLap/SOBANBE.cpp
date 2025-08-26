#include <iostream>
#include <cmath>
#include <iomanip>
using namespace std;

#define sn int
#define nhap cin
#define xuat cout
#define kt return 0

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

sn main (){
    sn n,m;
    nhap >> n >> m;
    if(tonguoc_khong_chinh(n) == m && tonguoc_khong_chinh(m) == n){
        xuat << "YES";  
    } else xuat << "NO";

}