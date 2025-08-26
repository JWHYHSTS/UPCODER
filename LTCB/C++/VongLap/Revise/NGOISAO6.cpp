/*
Viết chương trình in ra màn hình tam giác sao rỗng (nghĩa là chỉ in đường viền cạnh của tam giác) với chiều cao h nhập vào từ bàn phím.

Ví dụ:
Input:
3

Output:
  *  
 * * 
*****

Input:
5

Output:
    *    
   * *   
  *   *  
 *     * 
*********

Input:
6

Output:
     *     
    * *    
   *   *   
  *     *  
 *       * 
***********
Lưu ý: 

Xuất chính xác từng ký tự. Không xuất dư hoặc thiếu khoảng trắng, không xuất dư endl dòng cuối cùng.
*/

#include <iostream>
using namespace std;

int main(){
    int h;
    cin >> h;
    for(int i = 1; i <= h; i++){
        // In khoảng trắng trước ngôi sao
        for(int j = 1; j <= h - i; j++){
            cout << " ";
        }
        // In ngôi sao
        for(int j = 1; j <= 2*i - 1; j++){
            if(j == 1 || j == 2*i -1 || i == h){ // In ngôi sao ở đầu và cuối mỗi hàng, và ở hàng cuối cùng
                cout << "*";
            }else {
                cout << " ";
            }
        }
        // In khoảng trắng sau ngôi sao
        for(int j = 1; j <= h - i; j++){
            cout << " ";
        }
        if(i < h) cout << endl;
    }
    return 0;
}