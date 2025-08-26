/*
Nhập vào 2 số nguyên a và b.
Yêu cầu tìm UCLN của 2 số đó.

ví dụ
input:
10 8

output
2
*/
#include <iostream>
using namespace std;
int ucln(int a, int b){
    a = abs(a);
    b = abs(b);
    while(b != 0){
        int temp = a % b;
        a = b; 
        b = temp;
    }
    return a;
}
int bcnn(int a, int b){
    return (a*b) / ucln(a,b);
}
int main(){
    int a, b;
    cin >> a >> b;
    cout << ucln(a, b);
    // cout << bcnn(a,b);
    return 0;
}