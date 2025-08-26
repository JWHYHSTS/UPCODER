/*
Input:
- Dòng 1: Nhập vào N là số lượng phần tử của mảng
- Dòng 2: N số nguyên (mỗi số cách 1 khoảng trắng)

Ouput:
Yêu cầu xuất tổng các số chẵn trong mảng ra màn hình

ví dụ:
input:
4
1 2 3 4

output
6

*/
#include <iostream>
using namespace std;
int main(){
    int n = 0;
    cin >> n;
    int a[100];
    int tongch = 0;
    for(int i = 0; i < n; i++){
        cin >> a[i];
        if(a[i] % 2 == 0) tongch += a[i];
    }
    cout << tongch;
    return 0;
}