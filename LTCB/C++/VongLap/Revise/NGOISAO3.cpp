/*
Viết chương trình in ra màn hình hình chữ nhật sao rỗng với độ dài 2 cạnh nhập vào từ bàn phím.

Input: 2 số nguyên dương a, b.
Output: hình chữ nhật ngôi sao rỗng giữa tương ứng độ dài 2 cạnh.

Ví dụ:

Input:
3 5

Output:
*****
*   *
*****

Input:
5 8

Output:
********
*      *
*      *
*      *
********

Dữ liệu nhập đảm bảo vẽ được hình chữ nhật rỗng.

Lưu ý: 
Xuất chính xác từng ký tự. Không xuất dư hoặc thiếu khoảng trắng, không xuất dư endl dòng cuối cùng.
*/
#include <iostream>
using namespace std;

int main(){
    int a, b;
    cin >> a >> b;
    for(int i = 1; i <= a; i++){
        for(int j = 1; j <= b; j++){
            if(i == 1 || i == a || j == 1 || j == b){
                cout << "*";
            }else {
                cout << " ";
            }
        }
        if(i < a) cout << endl;
    }
    return 0;
}