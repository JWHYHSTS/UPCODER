/*
Nhap vào mot sô x, xác định sô x là sô dương, hay sô âm hoac bang 0 ?

Input:
- 1 số nguyên X

Output:
- Nếu X là số dương xuất kết quả: DUONG
- Nếu X là số âm xuất kết quả: AM
- Nếu X là số 0 xuất kết quả: KHONG

Ví dụ:
input:
3

output
DUONG

*/
#include <iostream>
using namespace std;
int main(){
    int x;
    cin >> x;
    if(x > 0) cout << "DUONG";
    else if(x < 0) cout << "AM";
    else cout << "KHONG";
    return 0;
}