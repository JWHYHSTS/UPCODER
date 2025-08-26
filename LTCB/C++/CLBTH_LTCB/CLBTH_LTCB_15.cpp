/*
Nhập 1 số nguyên dương N. Nhập tiếp N số nguyên.

Ghi ra màn hình dãy số vừa nhập.

Ghi ra màn hình dãy số vừa nhập theo thứ tự ngược lại.

Input:

Dòng đầu tiên chứa số nguyên dương N.

Dòng tiếp theo chứa N số nguyên dương x.

Output:

Dòng đầu tiên chứa dãy số vừa nhập.

Dòng tiếp theo chứa dãy số vừa nhập theo thứ tự ngược lại.

Ví dụ:


Input
4
1 3 4 2

Output
1 3 4 2
2 4 3 1

*/
#include <iostream>
using namespace std;
int main(){
    int n;
    cin >> n;
    int a[n];
    for(int i = 0; i < n; i++){
        cin >> a[i];
    }
    for(int i = 0; i < n; i++){
        cout << a[i] << " ";
    }
    cout << endl;
    for(int i = n - 1; i >= 0; i--){ // VD: n = 4 thì i sẽ chạy từ 3 đến 0 và in ra a[3], a[2], a[1], a[0]
        cout << a[i] << " ";
    }
    return 0;
}