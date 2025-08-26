/*
input:
- Nhập vào 1 số nguyên n

output:
- Nếu n là chẵn xuất "chan" ngược lại xuất "le"

ví dụ
input:
3

output:
le
*/
#include <iostream>
using namespace std;
int main(){
    int n;
    cin >> n;
    if(n % 2 == 0) cout << "chan";
    else cout << "le";
    return 0;
}