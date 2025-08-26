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

int ucln(long long a,long long b){
    while(b != 0){
        long long temp = a % b;
        a = b;
        b = temp;
    }
    return a;
}

int main(){
    long long a, b;
    cin >> a >> b;
    cout << ucln(a,b);
    return 0;
}