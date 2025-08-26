/*
Bộ 3 số Pytago

Như ta đã biết, với 3 số nguyên dương cho trước (a < b < c), nếu 3 số đó là độ dài 3 cạnh của một tam giác vuông thì bộ 3 số này được gọi là bộ 3 số Pytago.
Yêu cầu: 
Cho trước số nguyên dương n (n<= 10^4). Hãy xuất ra màn hình tất cả các bộ 3 số Pytago mà cả 3 số đều <= n (mỗi bộ số 1 dòng và xuất theo thứ tự tăng dần). Nếu không có thì xuất -1

Ví dụ:
Input
5
Ouput
3 4 5
Input
13
Output
3 4 5
5 12 13
6 8 10
*/

#include <iostream>
#include <iomanip>
#include <cmath>
using namespace std;

int main(){
    int n;
    cin >> n;
    bool found = false;
    for(int a = 1; a <= n; a++){
        for(int b = a + 1; b <= n; b++){
            // Tính c từ a và b (Vì Code của bạn bị TLE vì có độ phức tạp O(n³). Với n = 10⁴, sẽ có 10¹² phép tính. Đây là code tối ưu hóa:
            // Sử dụng công thức Pytago: c^2 = a^2 + b^2
            // Lưu ý: c phải là số nguyên dương và c <= n và c > b
            int c2 = a * a + b * b; // Tính c²
            int c = sqrt(c2); // Lấy căn bậc hai của c² để tìm c
            if(c * c == c2 && c <= n && c > b){ // Kiểm tra xem c có phải là số nguyên và c có lớn hơn b không
                cout << a << " " << b << " " << c << endl;
                found = true;
            }
        }
    }
    if(!found) cout << -1;
    return 0;
}