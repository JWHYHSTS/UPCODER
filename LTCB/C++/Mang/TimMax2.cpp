#include <iostream>
#include <cmath>
using namespace std;

#define sn int
#define nhap cin
#define xuat cout
#define kt return 0
#define MAX 1000000
#define MIN -1000000

sn main(){
    sn n, m;
    nhap >> n >> m;
    sn a[100][100];
    sn max = MIN;
    for(sn i = 0; i < n; i++){
        for(sn j = 0; j < m; j++){
            nhap >> a[i][j];
            if(a[i][j] > max) max = a[i][j];
        }
    }
    xuat << max;
    kt;
}