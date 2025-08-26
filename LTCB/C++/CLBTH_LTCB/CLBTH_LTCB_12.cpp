/*
Cho ba số a, b, c. Hãy kiểm tra xem ba số có thể tạo thành một cấp số nhân hay không.

Input:

Gồm một dòng chứa ba số nguyên dương a, b, c.

Output:

In ra YES nếu ba số tạo được một cấp số nhân, ngược lại in ra NO.

Ví dụ:
Input
1 9 3
Output
NO

// Cấp số nhân là một dãy số mà tỷ số giữa hai số liên tiếp là một hằng số. VD: 1 3 9 là cấp số nhân với tỷ số là 3.
*/
#include <iostream>
using namespace std;
int main(){
    int a, b, c;
    cin >> a >> b >> c;
    if(b * b == a * c) {
        cout << "YES";
    } else {
        cout << "NO";
    }
    return 0;
}
// Lý do dùng b * b == a * c là vì trong cấp số nhân, tỷ số giữa hai số liên tiếp là hằng số. Nếu a, b, c là cấp số nhân thì b^2 = a * c. ( a/b = b/c = c/a)