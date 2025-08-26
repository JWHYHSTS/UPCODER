/*
Input:
- Nhập vào 2 số nguyên N, M là số dòng và số cột của mảng 2 chiều NxM

Ouput:
Xuất mảng ZicZắc, các giá trị được đi từ 1 đến N.M (xem ví dụ để hiểu thêm)

Ví dụ:
input
3 3
output
1 2 3
6 5 4
7 8 9
*/

#include <iostream>
using namespace std;
int main(){
    int n, m;
    cin >> n >> m;
    int a[100][100];
    int dem = 1;
    for(int i = 0; i < n; i++){
        if(i % 2 == 0){ // Dòng chẵn thì đi từ trái sang phải và tăng dần
            for(int j = 0; j < m; j++){
                a[i][j] = dem++;
            }
        } else { // Dòng lẻ thì đi từ phải sang trái và tăng dần 
            for(int j = m - 1; j >= 0; j--){ // j = m - 1 để bắt đầu từ cột cuối cùng
                a[i][j] = dem++;
            }
        }
    }
// VD n = 3, m = 3
// a[0][0] = 1, a[0][1] = 2, a[0][2] = 3
// a[1][0] = 6, a[1][1] = 5, a[1][2] = 4
// a[2][0] = 7, a[2][1] = 8, a[2][2] = 9
    // Xuất mảng
    for(int i = 0; i < n; i++){
        for(int j = 0; j < m; j++){
            cout << a[i][j] << " ";
        }
        cout << endl;
    }
    return 0;
}