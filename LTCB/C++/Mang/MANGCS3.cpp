#include <iostream>
using namespace std;

#define sn int
#define nhap cin
#define xuat cout
#define kt return 0

sn main(){
    sn a[100];
    sn n;
    sn x;
    sn k;
    nhap >> k;
    while(nhap >> x){
        a[n] = x;
        n++;
    }
    // Xóa phần tử k
    for(sn i = k; i < n - 1; i++){ // Bắt đầu từ vị trí k, di chuyển các phần tử phía sau về trước 1 vị trí
        // VD: n = 5, k = 2, i = 2, 
        // a[2] = a[3], a[3] = a[4], a[4] = a[5]
        a[i] = a[i+1];
    }
    n--; // Giảm kích thước mảng đi 1 vì đã xóa phần tử tại vị trí k
    // In mảng sau khi xóa phần tử k
    for(sn i = 0; i < n; i++){
        xuat << a[i] << " ";
    }
    kt;
}