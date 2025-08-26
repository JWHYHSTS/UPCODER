/*
Input:
- Gồm nhiều ký tự (mỗi ký tự cách nhau 1 khoảng trắng) 
(chỉ tính các ký tự từ 'a' đến 'z', không tính khoảng trắng)

Output:
- Xuất số lượng các ký tự ra màn hình (xuất theo thứ tự từ nhỏ đến lớn - xem ví dụ để hiểu rõ hơn)

Ví dụ:

input
b a n a n a

output
a:3
b:1
n:2
Giải thích: 
ký tự 'a' xuất hiện 3 lần 
ký tự 'b' xuất hiện 1 lần 
ký tự 'n' xuất hiện 2 lần
*/
#include <iostream>
using namespace std;
int main(){
    int dem[26] = {0};
    char c;
    while(cin >> c) {
        if(c >= 'a' && c <= 'z'){
            dem[c - 'a']++; // Tăng số lượng ký tự tương ứng VD: // 'a' - 'a' = 0, 'b' - 'a' = 1, ..., 'z' - 'a' = 25
        }
    }
    for(int i = 0; i < 26; i++){
        if(dem[i] > 0){ 
            cout << char('a' + i) << ":" << dem[i] << endl; // VD: 'a' + 0 = 'a', 'a' + 1 = 'b', ..., 'a' + 25 = 'z'
        }
    }
    return 0;
}
