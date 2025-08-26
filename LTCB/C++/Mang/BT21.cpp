// Sắp xếp hàng trong mảng 2 chiều bằng hàm Sort
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

sn sort(sn a[], sn n){
    for(sn i = 0; i < n - 1; i++){
        for(sn j = i + 1; j < n; j++){
            if(a[i] > a[j]){
                swap(a[i], a[j]); // Sắp xếp tăng dần
            }
        }
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

    for(sn i = 0; i < n; i++){
        sort(a[i], m); // Sắp xếp từng hàng
    }

    for(sn i = 0; i < n; i++){
        for(sn j = 0; j < m; j++){
            xuat << a[i][j] << " ";
        }
        xuat << endl;
    }
    
    kt;
}