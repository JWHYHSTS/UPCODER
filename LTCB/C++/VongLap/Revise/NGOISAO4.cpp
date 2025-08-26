/*
Viết chương trình in ra màn hình tam giác sao cân với chiều cao h nhập vào từ bàn phím.

Ví dụ 1:

Input	Output
3
__*__
_***_
*****

Ví dụ 2:

Input	Output
5
____*____
___***___
__*****__
_*******_
*********

Ví dụ 3:

Input	Output
6
_____*_____
____***____
___*****___
__*******__
_*********_
***********

Lưu ý: 
Xuất chính xác từng ký tự. Không xuất dư hoặc thiếu khoảng trắng, không xuất dư endl dòng cuối cùng.
Các ký tự gạch nối màu đen (_) ở phía trên đại diện cho khoảng trắng mà các bạn phải xuất ra màn hình. Phải có các khoảng trắng này thì mới được tính là tam giác cân.
*/
#include <iostream>
using namespace std;

int main(){
    int h;
    cin >> h;
    for(int i = 1; i <= h; i++){
        // In khoảng trắng trước ngôi sao
        for(int j = 1; j <= h - i; j++){ // Lý do j <= h - i là để tạo ra khoảng trắng trước ngôi sao (VD: với h = 5, i = 1 thì có 4 khoảng trắng, i = 2 thì có 3 khoảng trắng, ...)
            cout << " ";
        }
        for(int j = 1; j <= 2*i - 1; j++){ // In ngôi sao, số lượng ngôi sao là 2*i - 1 (VD: với i = 1 thì có 1 ngôi sao, i = 2 thì có 3 ngôi sao, ...)
            cout << "*"; 
        }
        // In khoảng trắng sau ngôi sao
        for(int j = 1; j <= h - i; j++){
            cout << " ";
        }
        if(i < h) cout << endl; // Chỉ in xuống dòng nếu không phải là dòng cuối cùng
    }
    return 0;
}