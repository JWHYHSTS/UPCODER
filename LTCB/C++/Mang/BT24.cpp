// In ra ma trận chuyển vị 
#include <iostream>
#include <cmath>
#include <algorithm>
using namespace std;

#define sn int
#define nhap cin 
#define xuat cout 
#define kt return 0
#define Max 10000000
#define Min -10000000

void chuyenvi(sn a[][100], sn n, sn m){
    sn b[100][100];
    for(sn i = 0; i < n; i++){
        for(sn j = 0; j < m; j++){
            b[j][i] = a[i][j];
        }
    }
    for(sn i = 0; i < m; i++){
        for(sn j = 0; j < n; j++){
            xuat << b[i][j] << " ";
        }
        xuat << endl;
    }
}
sn main(){
    sn n,m;
    nhap >> n >> m;
    sn a[100][100];
    for(sn i = 0; i < n; i++){
        for(sn j = 0; j < m; j++){
            nhap >> a[i][j];
        }
    }
    xuat << "Ma tran chuyen vi la: " << endl;
    chuyenvi(a,n,m);
    kt;
}