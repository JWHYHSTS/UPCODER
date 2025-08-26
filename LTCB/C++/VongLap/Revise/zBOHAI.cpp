/*
Viết chương trình nhập vào 2 số nguyên dương N,M;  trong đó N có số chữ số lớn hơn một. Yêu cầu kiểm tra tích các chữ số của N có bằng tổng các ước của M hay không? Nếu có xuất YES ngược lại xuất NO

Dữ liệu nhập:

- Là hai số nguyên N, M cách nhau một khoảng trắng (1 ≤ N, M ≤ 105)

Dữ liệu xuất:

- In ra YES nếu N, M là thỏa điều kiện trên. In ra NO nếu không phải.

Ví dụ
Input
23 6
Output
NO
*/
#include <iostream>
using namespace std;
int tongUoc(int n){
    int tong = 0;
    for(int i = 1; i <= n; i++){ // Nếu i <= n thì sẽ tính cả n còn nếu i <= n/2 thì sẽ không tính n
        if(n%i == 0) tong += i;
    }
    return tong;
}

int tichChuSo(int n){
    int tich = 1;
    while(n > 0){
        tich *= n % 10;
        n /= 10;
    }
    return tich;
}

int main(){
    int n, m;
    cin >> n >> m;
    if(tichChuSo(n) == tongUoc(m)) cout << "YES";
    else cout << "NO";
    return 0;
}