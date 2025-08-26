/*
Nhập vào 1 số nguyên n, xuất ra n!

ví dụ:

input:
3

output:
6
*/
#include <iostream>
using namespace std;

int main(){
    int n;
    cin >> n;
    long long kq = 1;
    for(int i = 1; i <= n; i++){
        kq *= i;
    }
    cout << kq;
    return 0;
}