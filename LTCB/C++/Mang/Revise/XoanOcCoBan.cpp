/*
Input:
- Nhập vào 2 số nguyên N, M là số dòng và số cột của mảng 2 chiều NxM

Ouput:
Xuất mảng Xoắn Ốc, các giá trị được đi từ 1 đến N.M (xem ví dụ để hiểu thêm)

Ví dụ:
input
3 3
output
1 2 3
8 9 4
7 6 5

*/

#include <iostream>
using namespace std;

int main(){
    int n, m;
    cin >> n >> m;
    int a[100][100];
    int left = 0, right = m - 1, top = 0, bottom = n - 1;
    int dem = 1;
    while(left <= right && top <= bottom){
        // Di tu trai sang phai
        for(int i = left; i <= right; i++){
            a[top][i] = dem++;
        }
        top++;
        // Di tu tren xuong duoi
        for(int i = top; i <= bottom; i++){
            a[i][right] = dem++;
        }
        right--;
        // Di tu phai sang trai
        if(top <= bottom){
            for(int i = right; i >= left; i--){
                a[bottom][i] = dem++;
            }
            bottom--;
        }
        // Di tu duoi len tren
        if(left <= right){
            for(int i = bottom; i >= top; i--){
                a[i][left] = dem++;
            }
            left++;
        }
    }
    for(int i = 0; i < n; i++){
        for(int j = 0; j < m; j++){
            cout << a[i][j] << " ";
        }
        cout << endl;
    }
    return 0;
}