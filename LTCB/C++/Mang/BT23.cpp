// Tính tổng các phần tử trong tam giác dưới, trên của ma trận vuông (2 chiều)
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

sn tgiacduoi(sn a[][100], sn n){
    sn tong1 = 0;
    for(sn i = 0; i < n; i++){
        for(sn j = 0; j <= i; j++){ // Duyệt tam giác dưới
            tong1 += a[i][j];
        }
    }
    return tong1;
}

sn tgiactren(sn a[][100], sn n){
    sn tong2 = 0;
    for(sn i = 0; i < n; i++){
        for(sn j = i; j < n; j++){ // Duyệt tam giác trên
            tong2 += a[i][j];
        }
    }
    return tong2;
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
    sn tongtamgiacduoi = tgiacduoi(a, n);
    sn tongtamgiactren = tgiactren(a, n);
    xuat << "Tong cac pt trong tgiac duoi: " << tongtamgiacduoi << endl;
    xuat << "Tong cac pt trong tgiac tren: " << tongtamgiactren << endl;
    kt;
}