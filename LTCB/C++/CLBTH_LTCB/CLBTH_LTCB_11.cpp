/*
Cho một bảng A kích thước n hàng, m cột gồm các số nguyên dương. Hãy đưa ra tổng lớn nhất của một hàng và một cột.

Input:

Dòng đầu tiên chứa hai số n, m.

n dòng tiếp theo, mỗi dòng chứa m số mô tả bảng A.

Các số được nhập vào là các số nguyên dương không vượt quá 1000.

Output:

Dòng thứ nhất in ra tổng lớn nhất của một hàng bảng A.

Dòng thứ hai in ra tổng lớn nhất của một cột bảng A.

Ví dụ:


Input
2 3
2 4 5
9 9 2

Output
20
13

*/
#include <iostream>
using namespace std;
int main(){
    int n, m;
    cin >> n >> m;
    int a[n][m];
    for(int i = 0; i < n; i++){
        for(int j = 0; j < m; j++){
            cin >> a[i][j];
        }
    }
    int tonghang = 0, tongcot = 0;
    for(int i = 0; i < n; i++){
        int tong = 0;
        for(int j = 0; j < m; j++){
            tong += a[i][j];
        }
        if(tong > tonghang) tonghang = tong;
    }
    for(int j = 0; j < m; j++){
        int tong = 0;
        for(int i = 0; i < n; i++){
            tong += a[i][j];
        }
        if(tong > tongcot) tongcot = tong;
    }
    cout << tonghang << endl;
    cout << tongcot;
    return 0;
}