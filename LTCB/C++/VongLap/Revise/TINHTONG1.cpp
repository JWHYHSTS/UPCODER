/*
Input: 
1 số nguyên n
ouput: 
kết quả của phép toán: 1+1/2^3+1/3^3+...+1/n^3 
(kết quả lấy 3 chữ số thập phân)

ví dụ:
input:
3

output:
1.162
*/
#include <iostream>
#include <iomanip>
using namespace std;

int main(){
    cout << fixed << setprecision(3);
    int n;
    cin >> n;
    double tong = 0.0;
    for(int i = 1; i <= n; i++){
        tong += 1.0 / (i *i *i);
    }
    cout << tong + 1.0;
    return 0;
}