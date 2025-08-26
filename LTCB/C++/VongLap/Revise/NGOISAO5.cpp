/*
Viết chương trình in ra màn hình tam giác sao ngược với chiều cao h nhập vào từ bàn phím.

Ví dụ:
Input:
3

Output:
*****
 *** 
  *  

Input:
5

Output:
*********
 ******* 
  *****  
   ***   
    *    

Input:
6

Output:
***********
 ********* 
  *******  
   *****   
    ***    
     *     
Lưu ý: 
Xuất chính xác từng ký tự. Không xuất dư hoặc thiếu khoảng trắng, không xuất dư endl dòng cuối cùng.
*/
#include <iostream>
using namespace std;
int main(){
    int h;
    cin >> h;
    for(int i = 0; i < h; i++){
        // In khoảng trắng trước ngôi sao
        for(int j = 0; j < i; j++){ // Lý do j < i là để tạo ra khoảng trắng trước ngôi sao (VD: với h = 5, i = 0 thì không có khoảng trắng, i = 1 thì có 1 khoảng trắng, ...).
            cout << " ";
        }
        // In ngôi sao
        for(int j = 1; j <= 2*(h-i)-1; j++){ // Số lượng ngôi sao là 2*(h-i)-1 (VD: với h = 5 thì i = 0 có 9 ngôi sao, i = 1 có 7 ngôi sao, ...).
            cout << "*";
        }
        // In khoảng trắng sau ngôi sao
        for(int j = 0; j < i; j++){ // In khoảng trắng sau ngôi sao, số lượng khoảng trắng là i (VD: với h = 5 thì i = 0 có 0 khoảng trắng, i = 1 có 1 khoảng trắng, ...).
            cout << " ";
        }
        // Chỉ in xuống dòng nếu không phải là dòng cuối cùng
        if(i < h - 1) cout << endl;
    }
    return 0;
}