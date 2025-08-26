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

int UCLN(int a, int b){
    while(b != 0){ // Sử dụng thuật toán Euclid để tìm UCLN
        // Nếu b = 0 thì UCLN là a
        int temp = a % b; // Lấy phần dư của a chia cho b
        a = b; // Gán a bằng b
        b = temp; // Gán b bằng phần dư
    }
    return a;
}
// VD: UCLN(10, 8) sẽ trả về 2 (vì 10 % 8 = 2, sau đó 8 % 2 = 0, nên UCLN là 2) Thuật toán sẽ chạy như sau: temp = 10 % 8 = 2, a = 8, b = 2; tiếp tục với a = 8, b = 2: temp = 8 % 2 = 0, a = 2, b = 0; kết thúc vì b = 0, trả về a = 2.

int main(){
    int a, b;
    cin >> a >> b;
    cout << UCLN(a, b);
    return 0;
}