/*
Nhập vào 1 số nguyên, yêu cầu xuất ra chữ số hàng nghìn của số đó, nếu không có thì xuất ra -1.

Ví dụ:

Input
4315
Output
4
*/
#include <iostream>
using namespace std;

int main(){
    int n;
    cin >> n;
    if(n < 1000) cout << -1;
    else {
        int hn = (n / 1000) % 10;
        cout << hn;
    }
    return 0;
}