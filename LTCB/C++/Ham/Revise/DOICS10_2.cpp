/*
Yêu cầu xây dựng 1 lớp Ngăn xếp, sau đó áp dụng vào giải bài tập sau:
Nhập vào 1 số nguyên ở hệ 10, yêu cầu xuất ra 1 số ở hệ 2

Ví dụ:

Input

Output

10

1010


*/
#include <iostream>
#include <stack>
using namespace std;

int Dcs10_2(int n){
    if(n == 0){
        cout << "0";
        return 0;
    }
    stack<int>s;
    while(n > 0){
        s.push(n % 2);
        n /= 2;
    }
    while(!s.empty()){
        cout << s.top();
        s.pop();
    }
    return 0;
}

int main(){
    int n;
    cin >> n;
    Dcs10_2(n);
    return 0;
}