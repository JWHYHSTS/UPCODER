// Số Fibonacci 
#include <iostream>
#include <cmath>
using namespace std;

#define sn int
#define nhap cin
#define xuat cout
#define kt return 0

sn fib(sn n){
    if(n == 0 || n == 1) return 1;
    sn a = 0, b = 1, c;
    for(sn i = 2; i <= n; i++){
        c = a + b;
        a = b;
        b = c;
    }
    return c;
}

bool isFibo(sn n) {
    if(n == 0 || n == 1) return true;
    sn a = 0, b = 1, c;
    while (b <= n) {
        c = a + b;
        if (c == n) return true;
        a = b;
        b = c;
    }
    return false;
}

sn main(){
    sn n;
    nhap >> n;
    if(fib(n)) xuat << "YES";
    else xuat << "NO";
    xuat << endl;
    for(sn i = 0; i <= n; i++){
        if(isFibo(i)) xuat << i << " ";
    }
    xuat << endl;
    kt;
}