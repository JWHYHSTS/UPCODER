#include <iostream>
using namespace std;

#define sn int 
#define nhap cin 
#define xuat cout 
#define kt return 0 

sn main(){
    sn n,m;
    nhap >> n >> m;
    sn a[100][100];
    sn gtri = 1;
    sn top = 0, bottom = n - 1, left = 0, right = m - 1;
    while(top <= bottom && left <= right){
        for(sn j = left; j <= right; j++){
            a[top][j] = gtri++;
        }
        top++;
        for(sn i = top; i <= bottom; i++){
            a[i][right] = gtri++;
        }
        right--;
        if(top <= bottom){
            for(sn j = right; j >= left; j--){
                a[bottom][j] = gtri++;
            }
            bottom--;
        }
        if(left <= right){
            for(sn i = bottom; i >= top; i--){
                a[i][left] = gtri++;
            }
            left++;
        }
    }
    for(sn i = 0; i < n; i++){
        for(sn j = 0; j < m; j++){
            xuat << a[i][j] << " ";
        }
        xuat << endl;
    }
    kt;
}