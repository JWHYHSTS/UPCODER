// Tính tổng từng hàng, từng cột trong mảng 2 chiều
#include <iostream>
#include <cmath>
using namespace std;

#define sn int
#define nhap cin 
#define xuat cout 
#define kt return 0
#define Max 10000000
#define Min -10000000

sn tonghang(sn a[100][100], sn n, sn m){
    sn tongh = 0;
    for(sn i = 0; i < m; i++){
        tongh += a[n][i];
    }
    return tongh;
}

sn tongcot(sn a[100][100], sn n, sn m){
    sn tongc = 0;
    for(sn i = 0; i < n; i++){
        tongc += a[i][m];
    }
    return tongc;
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
    for(sn i = 0; i < n; i++){
        xuat << "Tong hang " << i + 1 << " = " << tonghang(a,i,m) << endl;
    }
    for(sn j = 0; j < m; j++){
        xuat <<"Tong cot " << j + 1 <<" = " << tongcot(a,n,j) << endl;
    }
    kt;
}