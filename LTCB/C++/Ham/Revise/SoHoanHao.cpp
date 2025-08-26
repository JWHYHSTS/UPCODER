/*
Số hoàn hảo là số mà tổng ước số của nó (không tính nó) bằng chính nó.
yêu cầu: nhập vào 1 số, xuất là Yes nếu nó là số hoàn hảo, ngược lại xuất No..

Ví dụ:

Input	Output
6
Yes
*/

#include <iostream>
using namespace std;
int shh(int n){
    int tong = 0;
    for(int i = 1; i <= n/2; i++){
        if(n % i == 0) tong += i;
    }
    return tong == n ? 1 : 0; 
}
int main(){
    int n;
    cin >> n;
    if(shh(n)) cout << "Yes";
    else cout << "No";
    return 0;
}