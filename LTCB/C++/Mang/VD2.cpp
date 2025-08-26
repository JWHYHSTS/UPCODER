// Mảng 2 chiều
#include <iostream>
#include <cmath>
using namespace std;

#define sn int
#define nhap cin
#define xuat cout
#define kt return 0

void nhapm2c(sn a[][100], sn n, sn m){
    for(sn i = 0; i < n; i++){
        for(sn j = 0; j < m; j++){
            nhap >> a[i][j];
        }
    }
}

void xuatm2c(sn a[][100], sn n, sn m){
    for(sn i = 0; i < n; i++){
        for(sn j = 0; j < m; j++){
            xuat << a[i][j] << " ";
        }
        xuat << endl;
    }
}

sn snt(sn n){
    if(n < 2) return 0;
    for(sn i = 2; i <= sqrt(n); i++){
        if(n%i == 0) return 0;
    }
    return 1;
}

sn dem(sn a[][100], sn n, sn m){
    sn dem = 0;
    for(sn i = 0; i < n; i++){
        for(sn j = 0; j < m; j++){
            if(snt(a[i][j])) 
            dem++;
        }
    }
    return dem;
}

sn main(){
    sn n,m;
    nhap >> n >> m;
    sn a[100][100];
    nhapm2c(a,n,m);
    xuat << "Ma tran vua nhap: " << endl;
    xuatm2c(a,n,m);
    xuat << "So luong so nguyen to trong ma tran: ";
    xuat << dem(a,n,m); 
    kt;
}