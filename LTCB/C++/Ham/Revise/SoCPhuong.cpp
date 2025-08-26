/*
Nhập vào 1 số.

Kiểm tra số đó có phải là số chính phương không?
Xuất: yes, nếu đó là số chính phương, ngược lại xuất no

ví dụ:
input: 4

output: yes
*/

#include <iostream>
#include <cmath>
using namespace std;

int scp(int n){
    int x = sqrt(n);
    if(x*x == n) return 1;
    return 0;
}

int main(){
    int n;
    cin >> n;
    if(scp(n)) cout << "yes";
    else cout << "no";
    return 0;
}