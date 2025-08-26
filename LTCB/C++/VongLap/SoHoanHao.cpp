#include <iostream>
#include <cmath>
using namespace std;

#define sn int
#define nhap cin
#define xuat cout
#define kt return 0

// số hoàn hảo là số mà tổng các ước số của nó (không bao gồm chính nó) bằng chính nó
int shh(sn n){
    sn tong = 0;
    for(sn i = 1; i <= n/2; i++){ // Nếu i <= n/2 thì sẽ không tính lại chính nó còn nếu tính cả chính nó thì i <= n // tính i = 1 là vì 1 là ước số của mọi số nguyên dương
        if(n % i == 0)
        tong += i;
    }
    return tong == n ? 1 : 0;
}
sn main(){
    sn n;
    nhap >> n;
    if(shh(n)) xuat <<"Yes";
    else xuat << "No";
    kt;
}