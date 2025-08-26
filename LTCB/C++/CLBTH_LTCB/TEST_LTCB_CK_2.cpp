/*
Cho mảng số nguyên a không quá 300 phần tử. Mỗi phần tử của mảng là một số nguyên có giá trị nằm trong đoạn từ [-100, 100]. Hãy in ra các phần tử không trùng lặp, theo đúng thứ tự xuất hiện lần đầu trong mảng.
Ví dụ: 

Input
4 3 8 3 3 1 4 2
Output
4 3 8 1 2

*/
#include <iostream>
using namespace std;
int main(){
    int a[300], n = 0;
    while (cin >> a[n]) n++;
    for (int i = 0; i < n; ++i) {
        bool appeared = false;
        for (int j = 0; j < i; ++j) {
            if (a[j] == a[i]) {
                appeared = true;
                break;
            }
        }
        if (!appeared) cout << a[i] << " ";
    }
    return 0;
}
