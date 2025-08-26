/*
Nhập vào 1 số nguyên, yêu cầu xuất ra chữ số ở vị trí i của số đó, nếu không có thì xuất ra -1
(Lưu ý thứ tự đếm từ trái sang phải - bắt đầu là vị trí thứ 0)

input:
- Dòng 1: Nhập vào vị trí thứ i cần xuất
- Dòng 2: Nhập vào số cần xử lý

output:
- Xuất ra chữ số thứ i, nếu không có xuất -1

ví dụ:
input:
1
1234

output
2
*/
#include <iostream>
using namespace std;
int main(){
    int n;
    string s;
    cin >> n >> s;
    //if(n < 0 || n >= s.length()){
    //    cout << -1;
    //}else cout << s[n];
    bool ktra = false;
    for(int i = 0; i < s.length(); i++){
        if(n == i){
            cout << s[i];
            ktra = true;
            break;
        }
    }
    if(!ktra) cout << -1;
    return 0;
}