/*
Năm 2024 là thế kỷ 21. Nhập vào số nguyên dương n, bạn hãy xác định xem năm n thuộc thế kỷ thứ mấy.

Input:

Một số nguyên n duy nhất.

Output:

Một số nguyên duy nhất là thế kỷ chứa năm n.

Ví dụ:


Input
2024
Output
21

*/

#include <iostream>
using namespace std;
int main(){
    int n;
    cin >> n;
    int tk = (n + 99) / 100; // Lý do (n + 99) / 100 vì một thế kỷ có 100 năm, và nếu n là năm cuối cùng của một thế kỷ thì ta cần cộng thêm 99 để đảm bảo tính đúng.
    cout << tk;
    return 0;
}