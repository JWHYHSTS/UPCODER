// Mảng 2 chiều - Tìm phần tử nhỏ nhất, lớn nhất trong mảng 
#include <iostream>
#include <cmath>
using namespace std;

#define sn int
#define nhap cin 
#define xuat cout 
#define kt return 0
#define Max 10000000
#define Min -10000000

sn main(){
    sn n,m;
    nhap >> n >> m;
    sn a[100][100];
    for(sn i = 0; i < n; i++){
        for(sn j = 0; j < m; j++){
            nhap >> a[i][j];
        }
    }
    
    sn gtmax = Min, gtmin = Max;
    for(sn i = 0; i < n ; i++){
        for(sn j = 0; j < m ; j++){
            if(a[i][j] < gtmin ) 
                gtmin = a[i][j];
            if(a[i][j] > gtmax)
            gtmax = a[i][j];    
        }
    }
    xuat << gtmax << endl;
    xuat << gtmin;
    kt;
}