// In ra chữ số chẵn đầu tiên tính từ bên phải của số tự nhiên n
#include <iostream>
using namespace std;

#define sn int
#define nhap cin
#define xuat cout
#define kt return 0

sn main(){
    sn n;
    nhap >> n;
    /* while (n != 0){
        if(n % 2 == 0){
            xuat << n % 10 << " ";
            break;
        }
        n /= 10; 
    }
        */
    for (; n != 0; n /= 10) {
    if (n % 2 == 0) {
        xuat << n % 10 << " ";
        break;
    }
}
    kt;
}