/*
Số hoàn hảo là số mà tổng ước số của nó (không tính nó) bằng chính nó.
yêu cầu: nhập vào 1 số, xuất là Yes nếu nó là số hoàn hảo, ngược lại xuất No..

Ví dụ:

Input	Output
6       Yes
*/

#include <iostream>
using namespace std;

int shh(int n){
    int sum = 0;
    for(int i = 1; i <= n/2; i++){ // Chỉ cần kiểm tra đến n/2 vì không có ước số nào lớn hơn n/2 ngoại trừ chính nó // i bắt đầu từ 1 vì 1 là ước số của mọi số nguyên dương
        if(n % i == 0){ // Nếu i là ước số của n
            sum += i;
        }
    }
    return sum == n ? 1 : 0; // Nếu tổng các ước số bằng n thì trả về 1 (Yes) là số hoàn hảo, ngược lại trả về 0 (No)
}

int main(){
    int n;
    cin >> n;
    if(shh(n)) cout << "Yes";
    else cout << "No";
    return 0;
}