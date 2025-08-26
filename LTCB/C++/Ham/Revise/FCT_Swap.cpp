/*
Viết chương trình nhập vào 2 số nguyên, sau đó hoán đổi giá trị của chúng cho nhau

Input: 
2 số nguyên a và b, mỗi số cách nhau 1 khoảng trắng
Output: 
2 số nguyên a và b đã hoán đổi giá trị, mỗi số cách nhau 1 khoảng trắng

Ví dụ:

Input	Output
2 3
3 2

*/
#include <iostream>
using namespace std;
int main() {
    int a, b;
    cin >> a >> b;
    swap(a, b);
    cout << a << " " << b;
    return 0;
}