/*
Giải phương trình Ax + B = 0. Với A, B là hai hệ sô kiểu số nguyên được nhập vào từ bàn phím

- Nếu phương trình vô nghiệm xuất kết quả: VN
- Nếu phương trình VSN xuất ra : VSN
- Nếu phương có nghiệm, xuất ra nghiệm (Lưu ý: kết quả xuất ra là số thực (lấy 2 chữ số thập phân)

Ví dụ:

Input	
2
-4
Output
2.00
2
3
Output
-1.50
*/
#include <iostream>
#include <iomanip>
using namespace std;

int main(){
    cout << fixed << setprecision(2);
    int a, b;
    cin >> a >> b;
    if(a == 0 && b != 0) cout << "VN";
    else if(a == 0 && b == 0) cout << "VSN";
    else {
        double x = -static_cast<double>(b) / a;
        cout << x;
    }
    return 0;
}