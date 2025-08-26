/*
TAM GIÁC SAO VUÔNG CÂN

Cho hình như sau:

*
**
***



Hình trên là 1 tam giác vuông cân được tạo từ các ký tự *.

Yêu cầu rất đơn giản, cho trước số ngôi sao, hãy xác định xem có thể xếp chúng thành một tam giác vuông cân được hay không.

 

Input

Một dòng chứa số nguyên N (1 <= N <= 10^18) là số ngôi sao.

 

Output

Một dòng chứa kết quả, nếu các ngôi sao có thể tạo thành tam giác vuông cân, in ra YES, ngược lại in ra NO

 

Ví dụ

input

3

output

YES

Giải thích:

Với n = 3, bạn có thể xếp được hình:

*

**

 

input

6

output

YES

Giải thích:

Với n = 6, bạn có thể xếp được hình:

*

**

***

 

input

5

output

NO
*/

#include <iostream>
using namespace std;

int main(){
    long long n;
    cin >> n;
    long long k = 0; // Số hàng của tam giác, ban đầu là 0
    // Sử dụng công thức n = k * (k + 1) /
    while(n > 0){ // Tiếp tục cho đến khi n không còn ngôi sao nào
        k++; // Tăng số hàng lên 1
        // Số ngôi sao cần cho hàng k là k
        n -= k; // Giảm số ngôi sao còn lại sau khi xếp hàng k
        // Nếu n < 0, có nghĩa là không đủ ngôi sao để xếp
    }
    if(n == 0){ // Nếu sau khi xếp hết các hàng, n còn lại là 0, tức là đã xếp hết ngôi sao
        cout << "YES"; // In ra YES nếu có thể xếp thành tam giác vuông cân
    } else {
        cout << "NO"; // In ra NO nếu còn ngôi sao không thể xếp thành hàng
    }
}