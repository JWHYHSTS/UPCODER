/*
Nhập vào từ bàn phím một số nguyên dương n. Hãy tìm và in ra màn hình chữ số lớn nhất của số n.

Input:

Một số nguyên dương n.

Output:

Đáp án của bài toán.

Ví dụ:


Input

Output

70128

8


*/
#include <iostream>
using namespace std;
int csln(int n){
    int max = 0;
    while(n > 0){
        int cs = n % 10;
        if(cs > max) max = cs;
        n /= 10;
    }
    return max;
}
int main(){
    int n;
    cin >> n;
    cout << csln(n);
    return 0;
}