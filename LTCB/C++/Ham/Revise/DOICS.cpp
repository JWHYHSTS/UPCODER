/*
Viết một hàm chuyển đổi cơ số từ hệ 10 sang hệ 2, 8 và 16 theo prototype sau:

void chuyenCoSo(long soHe10, int heCoSoMoi);

nếu tham số heCoSoMoi có giá trị là 0 thì chuyển sang cơ số 2, nếu là 1 thì chuyển sang hệ 8 còn nếu là 2 thì chuyển sang hệ 16.
Mặc định tham số heCoSoMoi có giá trị là 0.

ví dụ:
chuyenCoSo(10)   => kết quả sẽ là: 1010
chuyenCoSo(10,0)   => kết quả sẽ là: 1010
chuyenCoSo(10,1)   => kết quả sẽ là: 12
chuyenCoSo(10,2)   => kết quả sẽ là: A

Yêu cầu viết chương trình nhập vào 1 số nguyên n (0 < n <= 2000) là hệ cần đổi (theo qui ước của tham số là 0,1,2)
Xuất ra  số đã được đổi sang hệ tương ứng

Ví dụ:

Input	Output
10 0    1010
10 1    12
*/
    #include <iostream>
    #include <stack>
    using namespace std;

    int chuyenCoSo(long soHe10, int heCoSoMoi = 0) {
        if (soHe10 == 0) {
            cout << "0";
            return 0;
        }
        
        stack<int> s;
        while (soHe10 > 0) {
            s.push(soHe10 % (heCoSoMoi == 1 ? 8 : (heCoSoMoi == 2 ? 16 : 2)));
            soHe10 /= (heCoSoMoi == 1 ? 8 : (heCoSoMoi == 2 ? 16 : 2));
        }
        
        while (!s.empty()) {
            if (heCoSoMoi == 2 && s.top() >= 10) {
                cout << char(s.top() - 10 + 'A');
            } else {
                cout << s.top();
            }
            s.pop();
        }
        
        return 0;
    }
    int main() {
        long n;
        int heCoSo;
        cin >> n >> heCoSo;
        chuyenCoSo(n, heCoSo);
        return 0;
    }