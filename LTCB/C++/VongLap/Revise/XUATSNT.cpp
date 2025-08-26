/*
Nhập vào 1 số nguyên n, yêu cầu xuất tất cả số nguyên tố từ 1 đến n (mỗi số cách 1 khoảng trắng) - nếu không có số nào, xuất -1


ví dụ:

input:
5

output
2 3 5

*/

#include <iostream>
#include <cmath>
using namespace std;

int snt(int n){
    if(n < 2) return 0;
    for(int i = 2; i <= sqrt(n); i++){
        if(n % i == 0) return 0;
    }
    return 1;
}

int main(){
    int n;
    cin >> n;
    bool ktra = false;
    for(int i = 2; i <= n; i++){
        if(snt(i)){
            cout << i << " ";
            ktra = true;
        }
    }
    if(!ktra) cout << -1;
    return 0;
}