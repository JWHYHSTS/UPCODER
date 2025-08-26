/*
Input:
- Dòng 1: Nhập vào N là số lượng phần tử của mảng
- Dòng 2: N số nguyên (mỗi số cách 1 khoảng trắng)

Ouput:
Yêu cầu xuất tổng các số nguyên tố ra màn hình

ví dụ:
input:
3
1 2 3

output
5
*/
#include <iostream>
#include <cmath>
using namespace std;
int SNT(int n){
    if(n < 2) return 0;
    for(int i = 2; i <= sqrt(n); i++){
        if(n % i == 0) return 0;
    }
    return 1;
}

int main(){
    int n = 0;
    cin >> n;
    int a[100];
    int tong = 0;
    for(int i = 0; i < n; i++){
        cin >> a[i];
        if(SNT(a[i])) tong += a[i];
    }
    cout << tong;
    return 0;
}