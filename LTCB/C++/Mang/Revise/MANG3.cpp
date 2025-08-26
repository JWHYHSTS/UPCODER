/*
Input:
- Dòng 1: Nhập vào N là số lượng phần tử của mảng
- Dòng 2: N số nguyên (mỗi số cách 1 khoảng trắng)

Ouput:
Yêu cầu xuất tổng các số chính phương ra màn hình

ví dụ:
input:
4
1 2 3 4

output
5

*/

#include <iostream>
#include <cmath>
using namespace std;

int SCP(int n){
    if(n < 0) return 0;
    int x = sqrt(n);
    return (x * x == n) ? 1 : 0;
}

int main(){
    int n = 0; // đặt n = 0 để tránh lỗi khi nhập vào n < 0
    cin >> n;
    int a[100];
    int tong = 0;
    for(int i = 0; i < n; i++){
        cin >> a[i];
        if(SCP(a[i])) tong += a[i];
    }
    cout << tong;
    return 0;
}