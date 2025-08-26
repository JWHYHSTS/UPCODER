#include <iostream>
using namespace std;

#define sn int
#define nhap cin 
#define xuat cout 
#define kt return 0

sn main(){
    sn n;
    nhap >> n;
    sn a[n][n];
    for(sn i = 0; i < n; i++){
        for(sn j = 0; j < n; j++){
            nhap >> a[i][j];
            if(i == j) xuat << a[i][j] <<" "; // Đường chéo chính là các phần tử có chỉ số hàng bằng chỉ số cột (i == j)
        }
    }
    kt;
}
/*
Ma trận 3×3:
    j=0  j=1  j=2
i=0  ●    ○    ○     ← a[0][0]: i=0, j=0 → i==j ✓
i=1  ○    ●    ○     ← a[1][1]: i=1, j=1 → i==j ✓  
i=2  ○    ○    ●     ← a[2][2]: i=2, j=2 → i==j ✓
*/