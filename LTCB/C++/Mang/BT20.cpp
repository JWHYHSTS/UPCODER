// Bài toán hoán vị 2 hàng
#include <iostream>
#include <cmath>
using namespace std;

#define sn int
#define nhap cin 
#define xuat cout 
#define kt return 0
#define Max 10000000
#define Min -10000000

sn hoanvihang(sn a[][100], sn m, sn h1, sn h2){ 
    for(sn j = 0; j < m; j++){
        swap(a[h1][j], a[h2][j]); // Hoán vị từng phần tử trong 2 hàng
    }
    return 0;
}

sn hoanvicot(sn a[][100], sn n, sn c1, sn c2){
    for(sn i = 0; i < n; i++){
        swap(a[i][c1], a[i][c2]); // Hoán vị từng phần tử trong 2 cột)
    }
    return 0;
}

sn main(){
    sn n, m;
    nhap >> n >> m;
    sn a[100][100];
    for(sn i = 0; i < n; i++){
        for(sn j = 0; j < m; j++){
            nhap >> a[i][j];
        }
    }

    sn h1, h2;
    nhap >> h1 >> h2; // Nhập vào 2 hàng cần hoán vị (bắt đầu từ 0)
    hoanvihang(a,m,h1,h2);
    for(sn i = 0; i < n; i++){
        for(sn j = 0; j < m; j++){
            xuat << a[i][j] << " ";
        }
        xuat << endl;
    }
    sn c1, c2;
    nhap >> c1 >> c2; // Nhập vào 2 cột cần hoán vị (bắt đầu từ 0)
    hoanvicot(a,n,c1,c2);
    for(sn i = 0; i < n; i++){
        for(sn j = 0; j < m; j++){
            xuat << a[i][j] << " ";
        }
        xuat << endl;
    }
    kt;
}