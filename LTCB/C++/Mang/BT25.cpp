// Nhân 2 ma trận
#include <iostream>
using namespace std;

#define sn int
#define nhap cin 
#define xuat cout
#define kt return 0

void nhanMT(sn a[][100], sn b[][100], sn c[][100], sn m, sn n, sn p) {
    for (sn i = 0; i < m; i++) {
        for (sn j = 0; j < p; j++) {
            c[i][j] = 0;
            for (sn k = 0; k < n; k++) {
                c[i][j] += a[i][k] * b[k][j];
            }
        }
    }
}

sn main(){
    sn a[100][100], b[100][100], c[100][100];
    sn m, n, p;

    nhap >> m >> n;
    for (sn i = 0; i < m; i++) {
        for (sn j = 0; j < n; j++) {
            nhap >> a[i][j];
        }
    }

    nhap >> n >> p; 
    for (sn i = 0; i < n; i++) {
        for (sn j = 0; j < p; j++) {
            nhap >> b[i][j]; 
        }
    }

    nhanMT(a, b, c, m, n, p); 
    for (sn i = 0; i < m; i++) {
        for (sn j = 0; j < p; j++) {
            xuat << c[i][j] << " ";
        }
        xuat << endl;
    }

    kt;
}