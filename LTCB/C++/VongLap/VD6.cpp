// ĐẾM CHỮ SỐ CỦA SỐ TỰ NHIÊN N
#include <iostream>
using namespace std;

#define nt int
#define nhap cin
#define xuat cout
#define kt return 0

nt main(){
    int n;
    nhap >> n;
    int dem = 0;
    while(n != 0){
        dem++;
        n /=10; 
    }
    xuat <<dem; 
    kt;
}