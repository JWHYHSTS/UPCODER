// Đếm số cặp nguyên tố cùng nhau trong mảng
#include <iostream>
#include <cmath>
using namespace std;

#define sn int
#define nhap cin
#define xuat cout
#define kt return 0
#define MAX 10000000
#define MIN -10000000

sn ucln(sn a, sn b){
    while(b != 0){
        sn tmp = a % b;
        a = b;
        b = tmp;
    }
    return a;
}

sn main(){
    sn n;
    nhap >> n;
    sn a[n];
    for(sn i = 0; i < n; i++){
        nhap >> a[i];
    }
    sn dem = 0;
    for(sn i = 0; i < n - 1; i++){
        for(sn j = i + 1; j < n; j++){
            if(ucln(a[i], a[j]) == 1)
            xuat <<"(" << a[i] <<","<<a[j]<<")";
            dem++;
        }
    }
    xuat << endl;
    xuat << dem;
    kt;
}