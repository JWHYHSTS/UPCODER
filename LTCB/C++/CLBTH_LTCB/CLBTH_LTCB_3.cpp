/*
Cho hai số nguyên dương a, n. Tính an.   

Input:

Gồm một dòng chứa hai số nguyên dương a và n.

Dữ liệu đảm bảo an luôn luôn nhỏ hơn 10^19.

Output:

Giá trị an.

Ví dụ:


Input
2 3
Output
8

*/
#include <iostream>
using namespace std;
#define ll long long
int main(){
    ll a, n;
    cin >> a >> n;
    ll kq = 1;
    for(ll i = 1; i <= n; i++){
        kq *= a; // Tính a^n bằng cách nhân liên tiếp // VD: a = 2, n = 3 thì kq = 2 * 2 * 2 = 8
    }
    cout << kq;
    return 0;
}