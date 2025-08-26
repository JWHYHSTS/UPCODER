/*
Cau 2:
Input:
Nhập vào 1 số nguyên dương N (1<= N<=1000)
Output:
Xuất ra một dãy số nguyên dương (theo thứ tự tăng dần), bao gồm các số
hoặc là số lẻ hoặc là không phải là ước của N (nếu không tồn tại số nào
thì xuất ra -1) (các số nằm trong khoảng từ 1 đến N)
Ví dụ:
Input
10
Output
1 3 4 5 6 7 8 9
Giải thích: trong output:
các số 1, 3, 5, 7, 9 là số lẻ
các số 3, 4, 6, 7, 8, 9 là không phải là ước của 10
Các số này được xuất theo thứ tự tăng dần (những số trùng chỉ tính 1 lần): 1 3 4 5 6 7 8 9

*/

#include <iostream>
using namespace std;
int main(){
    int n;
    cin >> n;
    bool kt = false;
    for(int i = 1; i <= n; i++){
        if(i % 2 != 0 || n % i != 0){
            cout << i << " ";
            kt = true;
        }
    }
    if(!kt) cout << -1;
    return 0;
}

/*


#include <iostream>
using namespace std;

int main() {
    int n;
    cin >> n;

    if (n < 1 || n > 1000) {
        cout << "-1";
        return 0;
    }

    bool co = false;

    for (int i = 1; i <= n; i++) {
        if (i % 2 == 1 || n % i != 0) {
            cout << i << " ";
            co = true;
        }
    }

    if (!co) {
        cout << "-1";
    }

    return 0;
}

*/