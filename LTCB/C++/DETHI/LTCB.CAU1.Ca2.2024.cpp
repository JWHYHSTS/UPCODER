/*

Cau 1:
Viết chương trình nhập vào một số nguyên N và tính tích các số không chia
hết cho 3 trong dãy từ 1 đến N. Nếu N là 0 hoặc nhỏ hơn 0, in ra "N phai
la so nguyen duong".
Ví dụ:
Input
4
Output
8

*/

#include <iostream>
using namespace std;
int main(){
    int n;
    cin >> n;
    if(n <= 0) cout << "N phai la so nguyen duong";
    else {
        int tich = 1;
        for(int i = 1; i <= n; i++){
            if(i % 3 != 0) tich *= i;
        }
        cout << tich;
    }
    return 0;
}