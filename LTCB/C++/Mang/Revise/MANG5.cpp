/*
Input:
- Dòng 1: Nhập vào N là số lượng phần tử của mảng
- Dòng 2: N số nguyên (mỗi số cách 1 khoảng trắng)

Ouput:
- Dòng 1: xuất các số âm của dãy
- Dòng 2: xuất các số dương của dãy

Ví dụ:
input
4
1 -2 3 -4
output
-2 -4
1 3
*/

#include <iostream>
using namespace std;

int main(){
    int n = 0;
    cin >> n;
    int a[100];
    for(int i = 0; i < n; i++){
        cin >> a[i];
    }
    for(int i = 0; i < n; i++){
        if(a[i] < 0) cout << a[i] << " ";
    }
    cout << endl;
    for(int i = 0; i < n; i++){
        if(a[i] > 0) cout << a[i] << " ";
    }
    return 0;
}