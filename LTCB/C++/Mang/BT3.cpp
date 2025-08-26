// Tìm max, min trong mảng
#include <iostream>
#include <cmath>
using namespace std;

#define sn int
#define nhap cin
#define xuat cout
#define kt return 0
#define MAX 10000000
#define MIN -10000000

sn main(){
    sn n;
    nhap >> n;
    sn a[n];
    for(sn i = 0; i < n; i++){
        nhap >> a[i];
    }
    //sn max = a[0], min = a[0];
    sn max = MIN, min = MAX;
    for(int i = 1; i < n; i++){
        if(a[i] > max) max = a[i];
        if(a[i] < min) min = a[i];
    }
    xuat << max << endl;
    xuat << min;
    kt;
}