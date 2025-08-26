/*
Armstrong Numbers 1



Một số nguyên dương có n chữ số được gọi là số Armstrong khi tổng các lũy thừa bậc n của các chữ số của nó bằng chính nó.

Ví dụ:
371 là số Armstrong vì: 3^3 + 7^3 + 1^3 = 371
8208 là số Armstrong vì: 8^4 + 2^4 + 8^4 = 8208
Hãy kiểm tra xem một số nguyên dương N nhập vào từ bàn phím có phải là số Armstrong hay không?
 
Input:
Gồm nhiều dòng, mỗi dòng là một số nguyên dương N (1 <= N <= 10.000.000)
Output:
Gồm nhiều dòng, mỗi dòng là câu trả lời cho từng số N ở trên. Nếu N là số Armstrong thì xuất “YES”. Ngược lại xuất “NO” (không xuất dấu ngoặc kép)
 
Ví dụ:
Input:
371
123
8208
 
Output:
YES
NO
YES
*/

#include <iostream>
#include <cmath>
using namespace std;

bool isArmstrong(int n){
    int bandau = n;
    int tong = 0;
    int cs = 0;
    // Đếm số chữ số
    while (n > 0){
        n /= 10; // Chia n cho 10 để loại bỏ chữ số cuối và n sẽ giảm dần và bị giảm về 0
        cs++;
    }
    n = bandau; // Khôi phục lại giá trị ban đầu của n (Lý do là n đã bị thay đổi trong vòng lặp trên)
    // Tính tổng các chữ số lũy thừa bậc cs
    while(n > 0){
        int chuSo = n % 10;
        tong += pow(chuSo, cs);
        n /= 10;
    }
    return tong == bandau; // So sánh tổng với giá trị ban đầu. Nếu bằng thì là số Armstrong
}

int main(){
    int n;
    while(cin >> n){
        if(isArmstrong(n)) cout << "YES" << endl;
        else cout << "NO" << endl;
    }
    return 0;
}