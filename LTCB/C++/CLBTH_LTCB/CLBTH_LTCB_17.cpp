/*
Cho bốn số thực A, B, C, D. Hỏi tích của bốn số đó là số dương, số âm hay số 0.

Input:

Gồm bốn dòng, mỗi dòng gồm một số thực lần lượt là bốn số A, B, C, D. (-10^18 ≤ A, B, C, D ≤ 1018).

Output:

Một số nguyên duy nhất là:

1 nếu tích bốn số là số dương.

-1 nếu tích bốn số là số âm.

0 nếu tích bốn số là số 0.

Ví dụ:


Input
20.21
-1.2
-2.3
1.0

Output
1


Ví dụ:


Input 2
5.0
-8.9
0.0
123.456

Output 2
0


*/

#include <iostream>
using namespace std;
int main(){
    double a, b, c, d;
    cin >> a >> b >> c >> d;
    double tich = a * b * c * d;
    if(tich >= 1) cout << 1;
    else if(tich <= -1) cout << -1;
    else cout << 0;
    return 0;
}