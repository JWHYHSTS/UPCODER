/*
Nhập vào 1 số.

Kiểm tra số đó có phải là số chính phương không?
Xuất: yes, nếu đó là số chính phương, ngược lại xuất no ( Số chính phương là số có căn bậc hai là một số nguyên). VD: 4 là số chính phương vì căn bậc hai của 4 là 2, và 2 là số nguyên.

ví dụ:
input: 4

output: yes
*/
#include <iostream>
#include <cmath>
using namespace std;

int SCP(int n) {
    if(n < 0) return 0; // nếu n < 0 thì không phải số chính phương
    int a = sqrt(n);
    if(a * a == n) return 1; // Nếu căn bậc hai của n bình phương lại bằng n thì là số chính phương
    return 0;
}
/*
Cách 2: 
int SCP(int n){
    int sqrt_n = sqrt(n);
    return (sqrt_n * sqrt_n == n) ? 1 : 0; // Trả về 1 nếu là số chính phương, ngược lại trả về 0
}
*/

int main() {
    int n;
    cin >> n;
    if(SCP(n)) cout << "yes";
    else cout << "no";
    return 0;
}