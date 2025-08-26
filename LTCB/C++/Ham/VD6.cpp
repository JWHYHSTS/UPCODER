// Tính tổng ước và đếm các ước của N
#include <iostream>
#include <cmath>
using namespace std;

#define sn int
#define nhap cin 
#define xuat cout 
#define kt return 0

sn tonguoc(sn n){
    sn tong = 0;
    for(sn i = 1; i <= sqrt(n); i++){
        if(n%i == 0){
            tong += i;
            if(i != n/i){
                tong += n /i;
            }
        }
    }
    return tong;
}

sn demuoc(sn n){
    sn dem = 0;
    for(sn i = 1; i <= sqrt(n); i++){
        if(n % i == 0){
            dem++;
            if(i != n / i){
                dem++;
            }
        }
    }
    return dem;
}

sn main(){
    sn n;
    nhap >> n;
    xuat << tonguoc(n) <<" "<< demuoc(n); 
    kt;
}