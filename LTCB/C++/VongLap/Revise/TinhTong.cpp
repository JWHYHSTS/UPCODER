/*
Nhập vào 1 dãy số, yêu cầu tính tổng các chữ số của dãy đó.

ví dụ:
input:
1
12
23
output:
1
3
5
*/

#include <iostream>
using namespace std;

int Tongcs(int n){
    int tong = 0;
    while(n > 0){
        tong += n % 10;
        n /= 10;
    }
    return tong;
}
int main(){
    int n;
    while(cin >> n){
        cout << Tongcs(n) << endl;
    }
    return 0;
}