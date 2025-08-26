/*
Cho số nguyên n. Tính n! = 1 × 2 × 3 × 4 × … × n.

Input:

Gồm một số nguyên n duy nhất (n ≤ 20).

Output:

Giá trị của n!

Lưu ý: 0! = 1

Ví dụ:

Input
5
Output
120
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