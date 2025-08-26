/*

Cho hai điểm A(xA, yA) và B(xB, yB) trên mặt phẳng tọa độ Oxy. Hãy tính khoảng cách giữa hai điểm A và B.

Input:

Gồm một dòng chứa 4 số thực xA, yA, xB, yB.

Output:

In ra khoảng cách giữa hai điểm A(xA, yA) và B(xB, yB). Kết quả lấy chính xác 3 chữ số sau dấu thập phân.

Ví dụ:


Input

Output

1 1 4 5

5.000

*/

#include<iostream>
#include <cmath>
#include <iomanip>
using namespace std;
int main(){
    cout << fixed << setprecision(3);
    double x1, y1, x2, y2;
    cin >> x1 >> y1 >> x2 >> y2;
    double kc = sqrt(pow(x2 - x1, 2) + pow(y2 - y1, 2));
    cout << kc;
    return 0;
}