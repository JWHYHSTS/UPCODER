/*
Nhập vào số n.

Xuất tổng từ 1 đến n
*/
#include <iostream>
using namespace std;

int main(){
    int n;
    cin >> n;
    int tong = 0;
    for(int i = 1; i <= n; i++){
        tong += i;
    }
    cout << tong;
    return 0;
}