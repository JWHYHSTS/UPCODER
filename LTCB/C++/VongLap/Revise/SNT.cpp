/*
Nhập vào 1 số.

Kiểm tra số đó có phải là số nguyên tố không?
Xuất: true, nếu đó là số nguyên tố, ngược lại xuất false

Ví dụ:

Input	Output
4       false

*/

#include <iostream>
#include <cmath>
using namespace std;

int snt(int n){
    if(n < 2) return 0; // Số nguyên tố nhỏ nhất là 2
    for(int i = 2; i <= sqrt(n); i++){
        if(n % i == 0) return 0; // Nếu n chia hết cho i thì n không phải là số nguyên tố
    }
    return 1;
}
int main(){
    int n;
    cin >> n;
    if(snt(n)) cout << "true";
    else cout << "false";
    return 0;
}