/*
Nhập vào số n.

Xuất tổng các số lẻ từ 1 đến n
*/
#include <iostream>
using namespace std;
int main(){
    int n;
    cin >> n;
    int tong = 0;
    for(int i = 1; i<= n; i+=2) { // Cách 2: for(int i = 1; i <= n; i++) if(i % 2 != 0) tong += i; 
        tong += i;
    }
    cout << tong;
    return 0;
}