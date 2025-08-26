/*
Viết chương trình nhập vào số nguyên dương n, in ra giá trị của tổng sau
1 + 2/3 + 2/3 * 4/5 + 2/3 * 4/5 * 6/7 + ... + 2/3 * 4/5 * ... * 2(n+1)/(2n+3)




Ví dụ:  

input
3
output
3.06

Lưu ý: kết quả lấy 2 chữ số thập phân
*/
#include <iostream>
#include <iomanip>
using namespace std;

int main(){
    cout << fixed << setprecision(2);
    double n, tong = 1, tich = 1;
    cin >> n;
    for(int i = 0; i <= n; i++){ // i là số hạng thứ i 
        tich = 1; // reset tich về 1 cho mỗi số hạng
        // Tính tích của các số hạng từ 0 đến i
        for(int j = 0; j <= i; j++){ // j là chỉ số của các số hạng trong tích
            // Công thức tính từng số hạng: 2*(j+1)/(2*j
            tich *= (double)(2*(j+1)) / (2*j+3); 
        }
        tong += tich; // cộng dồn vào tổng
    }
    cout << tong;
    return 0;
}