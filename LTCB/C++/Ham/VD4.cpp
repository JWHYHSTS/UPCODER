// In ra các số chính phương từ 1 tới N (Số chính phương là số có căn bậc hai là một số nguyên)
#include <iostream>
#include <cmath>
using namespace std;

#define sn int
#define nhap cin
#define xuat cout
#define kt return 0

sn scp(sn n){
    sn cbh = sqrt(n);
    if(cbh * cbh == n) return 1;
    return 0;
}

sn main(){
    sn n;
    nhap >> n;
    sn dem = 0;
    for(sn i = 1; i <= n; i++){
        if(scp(i)){
        xuat << i << " ";
        dem++;
        }
    }
    xuat << endl;
    xuat << dem;
    kt;
}