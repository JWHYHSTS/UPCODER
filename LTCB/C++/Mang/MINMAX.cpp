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
    sn a[100];
    sn n;
    sn x;
    while(nhap >> x){
        a[n] = x;
        n++;
    }
    sn max = MIN, min = MAX;
    for(sn i = 0; i < n; i++){
        if(a[i] > max) max = a[i];
        if(a[i] < min) min = a[i];
    }
    xuat << min << endl;
    xuat << max << endl;
    sn tong = max + min;;
    xuat << tong;
    kt;
        
}