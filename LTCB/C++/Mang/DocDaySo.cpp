#include <iostream>
#include <algorithm>
using namespace std;

#define sn int
#define nhap cin 
#define xuat cout 
#define kt return 0

sn main(){
    sn a[100];
    sn n = 0;
    sn x;
    sn tong = 0;
    while(nhap >> x){
        a[n] = x;
        n++;
    }
    for(sn i = 0; i < n; i++){
        tong += a[i];
    }
    // Sắp xếp mảng a theo thứ tự tăng dần
    for(sn i = 0; i < n - 1; i++){
        for(sn j = 0; j < n - 1 - i; j++){ // j < n - 1 - i để tránh so sánh các phần tử đã được sắp xếp
            if(a[j] > a[j+1]){ // So sánh hai phần tử liên tiếp
                swap(a[j], a[j+1]);
            }
        }
    }
    if(n < 3) { xuat << "NO"; kt;}
    xuat << n << endl;
    xuat << tong << endl;
    for(sn i = 0; i < n; i++){
        xuat << a[i] <<" ";
    }
    kt;
}