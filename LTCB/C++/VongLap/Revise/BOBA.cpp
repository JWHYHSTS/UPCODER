/*
Viết chương trình nhập vào 3 số nguyên dương N,M,K; 

Yêu cầu kiểm tra tổng các chữ số của N cộng với chữ số đầu tiên của M có bằng K hay không? Nếu có xuất Yes ngược lại xuất No

Dữ liệu nhập:

- Là 3 số nguyên N, M, K cách nhau một khoảng trắng (1 ≤ N, M,K ≤ 105)

Dữ liệu xuất:

- In ra Yes nếu N, M là thỏa điều kiện trên. In ra No nếu không phải.

Ví dụ
Input
23 123 6
Output
Yes
*/

#include <iostream>
using namespace std;

int tongchuso(int n){
    int tong = 0;
    while(n > 0){
        tong += n % 10;
        n /= 10;
    }
    return tong;
}
int csdt(int n){
    while(n >= 10){
        n /= 10;
    }
    return n;
}

int main(){
    int n, m, k;
    cin >> n >> m >> k;
    if(tongchuso(n) + csdt(m) == k) cout << "Yes";
    else cout << "No";
    return 0;
}