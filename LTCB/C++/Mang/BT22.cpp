// Liệt kê các số nguyên tố trên đường chéo chính và đường chéo phụ của ma trận
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

sn snt(sn n){
    if(n < 2) return 0;
    for(sn i = 2; i <= sqrt(n); i++){
        if(n % i == 0) return 0;
    }
    return 1;
}

sn main(){
    sn n, m;
    nhap >> n >> m;
    sn a[n][m];
    for(sn i = 0; i < n ; i++){
        for(sn j = 0; j < m; j++){
            nhap >> a[i][j];
        }
    }
    xuat << "Cac snt tren duong cheo chinh la: ";
    for(sn i = 0; i < n; i++){
        if(snt(a[i][i])){
            xuat << a[i][i] << " ";
        }
    }
    xuat << endl;
    xuat << "Cac snt tren duong cheo phu la: ";
    for(sn i = 0; i < n; i++){
        if(snt(a[i][n - i - 1])){ 
        xuat << a[i][n - i - 1] << " ";
// n - i - 1 là chỉ số cột của đường chéo phụ Với ma trận 4x4 (n = 4): ( Ta có i + j = n - 1)
// i	j = n - i - 1
// 0	3
// 1	2
// 2	1
// 3	0
        }
    }
    kt;

}