// Cộng trừ hai ma trận
#include <iostream>
using namespace std;

#define sn int
#define nhap cin 
#define xuat cout 
#define kt return 0

void tong(sn a[][100], sn b[][100], sn c[][100], sn n, sn m){
    for(sn i = 0; i < n; i++){
        for(sn j = 0; j < m; j++){
            c[i][j] = a[i][j] + b[i][j];
        }
    }
}

void hieu(sn a[][100], sn b[][100], sn d[][100], sn n, sn m){
    for(sn i = 0; i < n; i++){
        for(sn j = 0; j < m; j++){
            d[i][j] = a[i][j] - b[i][j];
        }
    }
}

sn main(){
    sn n, m;
    nhap >> n >> m;
    sn a[100][100], b[100][100];
    for(sn i = 0; i < n; i++){
        for(sn j = 0; j < m; j++){
            nhap >> a[i][j];
        }
    }
    sn k, l;
    nhap >> k >> l;
    for(sn i = 0; i < n; i++){
        for(sn j = 0; j < m; j++){
            nhap >> b[i][j];
        }
    }
    sn c[100][100], d[100][100];
    tong(a, b, c, n, m);
    hieu(a, b, d, n, m);

    xuat << "Tong 2 mt:\n";
    for(sn i = 0; i < n; i++){
        for(sn j = 0; j < m; j++){
            xuat << c[i][j] << " ";
        }
        xuat << endl;
    }
    xuat << "Hieu 2 mt:\n";
    for(sn i = 0; i < n; i++){
        for(sn j = 0; j < m; j++){
            xuat << d[i][j] << " ";
        }
        xuat << endl;
    }
    kt;
}