/*
Nhap vào 2 sô nguyên a,b. Xuất sô lớn nhât

ví dụ:
input 
2 3

output
3

*/
#include <iostream>
using namespace std;
int main() {
    int a, b;
    cin >> a >> b;
    if(a > b) cout << a;
    else cout << b;
    return 0;
}