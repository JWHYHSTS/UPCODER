/*
Viết chương trình in ra màn hình hình chữ nhật sao với độ dài 2 cạnh nhập vào từ bàn phím.

Input: 2 số nguyên dương a, b.
Output: hình chữ nhật ngôi sao tương ứng độ dài 2 cạnh.

Ví dụ:

Input:
3 5

Output:
*****
*****
*****
Lưu ý:  Xuất chính xác từng ký tự. Không xuất dư hoặc thiếu khoảng trắng, không xuất dư endl dòng cuối cùng.
*/

#include <iostream>
using namespace std;

int main(){
    int a, b;
    cin >> a >> b;
    for(int i = 1; i <= a; i++){
        for(int j = 1; j <= b; j++){
            cout << "*";
        }
        if(i < a) cout << endl; // Chỉ in xuống dòng nếu không phải là dòng cuối cùng
    }
    return 0;
}

/*
#include <iostream>
using namespace std;
int main(){
    int a, b;
    cin >> a >> b;
    for(int i = 0; i < a; i++){
        for(int j = 0; j < b; j++){
            cout << "*";
        }
        if(i < a - 1) cout << endl;
    }
}
*/