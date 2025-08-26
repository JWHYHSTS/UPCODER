// Liệt kê các số Fibonacci trong mảng 2 chiều
#include <iostream>
#include <cmath>
using namespace std;

#define sn int
#define nhap cin 
#define xuat cout 
#define kt return 0
#define Max 10000000
#define Min -10000000

bool fib(sn n){
    if(n == 0 || n == 1) return true;
    sn a = 0, b = 1, c;
    while(b < n){
        c = a + b;
        a = b;
        b = c;
    }
    return (b == n);
}

sn main(){
    sn n,m;
    nhap >> n >> m;
    sn a[100][100];
    for(sn i = 0; i < n; i++){
        for(sn j = 0; j < m; j++){
            nhap >> a[i][j];
        }
    }

    for(sn i = 0; i < n; i++){
        for(sn j = 0; j < m; j++){
            if(fib(a[i][j])){
                xuat << a[i][j] << " ";
            }
        }
    }
    kt;
}