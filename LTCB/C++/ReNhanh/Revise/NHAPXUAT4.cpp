/*
Nhập vào 1 số nguyên, yêu cầu xuất ra chữ số hàng trăm của số đó, nếu không có thì xuất ra -1


ví dụ:
input:
1234

output
2
*/
#include <iostream>
using namespace std;

int main(){
    int n;
    cin >> n;
    if(n < 100) cout << -1;
    else {
        int ht = (n / 100) % 10;
        cout << ht;
    }
    return 0;
}
