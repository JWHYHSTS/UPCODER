/*
Input:
- 2 số nguyên N, M.

Output:
- Nếu 2 số N,M nguyên tố cùng nhau xuất "yes", ngược lại xuất "no"

Ví dụ:

input
2 3

output
yes
*/
#include <iostream>
#include <algorithm>
using namespace std;
int gcd(int a, int b) {
    while (b != 0) {
        int t = a % b;
        a = b;
        b = t;
    }
    return a;
}
bool CSNT(int a, int b) {
    return gcd(a, b) == 1;
}  
int main() {
    int N, M;
    cin >> N >> M;
    if (CSNT(N, M)) {
        cout << "yes";
    } else {
        cout << "no";
    }
    return 0;
}