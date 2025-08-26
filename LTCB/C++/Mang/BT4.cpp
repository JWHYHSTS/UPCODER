// Mảng đối xứng & Lật ngược mảng
#include <iostream>
#include <cmath>
using namespace std;

#define sn int
#define nhap cin
#define xuat cout
#define kt return 0
#define MAX 10000000
#define MIN -10000000

sn dx(sn a[], sn n){
    for(sn i = 0; i < n/2 ; i++){ // i < n/2 vì mảng đx chỉ cần ss nửa đầu với nửa sau
        if(a[i] != a[n-1-i]) return 0; // Nếu có phần tử nào không bằng thì mảng không đối xứng
    }
    return 1;
}

sn lm(sn a[], sn n){ // Hàm lật ngược mảng
    for(sn i = 0; i < n/2; i++){
        sn tmp = a[i];
        a[i] = a[n-1-i];
        a[n-1-i] = tmp;
    }
    return 1;
}
sn main(){
    sn n;
    nhap >> n;
    sn a[n];
    for(sn i = 0; i < n; i++){
        nhap >> a[i];
    }
    if(dx(a,n)) xuat << "MDX";
    else xuat << "MKDX";
    xuat << endl;
    lm(a,n);
    for(sn i = 0; i < n; i++){
        xuat << a[i] << " ";
    }
    kt;
}