/*
Cho hai số nguyên không âm a và b, hãy tìm ước số chung lớn nhất của a và b.



Dữ liệu nhập:

Gồm 2 số a và b cách nhau một khoảng trắng (0 ≤ a, b ≤ 10^18)

Dữ liệu xuất:

Số nguyên dương duy nhất là ước số chung lớn nhất của a và b.


Ví dụ:

Input
6 9
Output
3

Input
1 10
Output
1
*/
#include <iostream>
using namespace std;
#define ll long long

ll UCLN(ll a, ll b){ // Dùng ll vì đề yêu cầu b <= 10^18
    a = abs(a); // lấy giá trị tuyệt đối của a để tránh trường hợp a < 0
    b = abs(b); // lấy giá trị tuyệt đối của b để tránh trường hợp b < 0
    while(b != 0){
        ll temp = a % b;
        a = b;
        b = temp;
    }
    return a;
}

int main(){
    ll a, b;
    cin >> a >> b;
    cout << UCLN(a, b);
    return 0;
}