/*
Nhập vào 1 dãy số, yêu cầu tính tổng các chữ số nguyên tố của dãy đó.

ví dụ:
input:
1
12
23
output:
0
2
5
*/

#include <iostream>
#include <cmath>
using namespace std;

int snt(int n){
    if(n < 2) return 0;
    for(int i = 2; i <= sqrt(n); i++){
        if(n % i == 0) return 0;
    }
    return 1;
}

int Tongcsnt(int n){
    int tong = 0;
    while(n > 0){
        int cs = n % 10; // Lấy chữ số cuối cùng
        if(snt(cs)){
            tong += cs;
        }
        n /= 10; // Bỏ chữ số cuối cùng
    }
    return tong;
}

int main(){
    int n;
    while(cin >> n){
        cout << Tongcsnt(n) << endl;
    }
    return 0;
}