// Liệt kê các cặp có tổng bằng K cho trước
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
    sn n, k;
    nhap >> n >> k;
    sn a[n];
    for(sn i = 0; i < n; i++){
        nhap >> a[i];
    }
    for(sn i = 0; i < n; i++){
        for(sn j = i + 1; j < n; j++){
            if(a[i] + a[j] == k){
                xuat << "(" << a[i] << ","<< a[j] <<")";
            }
        }
    }
    kt;
}