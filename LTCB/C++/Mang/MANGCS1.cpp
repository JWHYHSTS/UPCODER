#include <iostream>
using namespace std;

#define sn int
#define nhap cin 
#define xuat cout 
#define kt return 0

sn main(){
    sn k,x;
    nhap >> k >> x;
    sn n;
    sn a[100]; 
    sn temp;
    while(nhap >> temp){
        a[n] = temp;
        n++;
    }
    for(sn i = n - 1; i >= k; i--){ // i = n - 1 có nghĩa là bắt đầu từ phần tử cuối cùng    // i > = k dùng để chèn vào vị trí k // VD: n = 5, k = 2, i = 4, a[4] = a[3], a[3] = a[2], a[2] = a[1], a[1] = a[0]
        a[i+1] = a[i]; // VD: n = 5, k = 2, i = 4, a[5] = a[4], a[4] = a[3], a[3] = a[2], a[2] = a[1], a[1] = a[0]
    }
    a[k] = x;
    n++; // Tăng kích thước mảng lên 1 vì đã chèn thêm phần tử mới vào vị trí k
    for(sn i = 0; i < n; i++){
        xuat << a[i] <<" ";
    }
    kt;
}
