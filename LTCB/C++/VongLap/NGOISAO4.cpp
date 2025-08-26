// Viết chương trình in ra màn hình tam giác sao cân với chiều cao h nhập vào từ bàn phím.
#include <iostream>
using namespace std;

#define sn int
#define nhap cin
#define xuat cout
#define kt return 0

sn main(){
    sn n;
    nhap >> n;
    
    for(sn i = 0; i < n; i++){
        for(sn j = 1; j < 2*n; j++){
            if(j < n - i || j > n+i) xuat <<" ";
            else xuat <<"*";
        }
        if(i != n -1) xuat << endl;
    }
    kt;
}