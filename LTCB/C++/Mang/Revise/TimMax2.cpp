/*
Tìm giá trị lớn nhất trong mảng 2 chiều NxM

Input:
- Dòng 1: Nhập vào 2 số nguyên N, M là số dòng và số cột của mảng 2 chiều NxM
- N dòng tiếp theo, mỗi dòng là M số nguyên.

Ouput:
Giá trị lớn nhất trong mảng NxM

Ví dụ:
input
3 3
1 1 3
6 1 4
7 5 9
output
9
*/

#include <iostream>
using namespace std;
#define MIN - 1000000

int main(){
    int n, m;
    cin >> n >> m;
    int a[100][100];
    int max = MIN;
    for(int i = 0; i < n; i++){
        for(int j = 0; j < m; j++){
            cin >> a[i][j];
            if(a[i][j] > max) max = a[i][j];
        }
    }
    cout << max;
    return 0;
}