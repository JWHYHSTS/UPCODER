/*
xây dựng 1 cấu trúc Phân Số (gồm tử và mẫu là số nguyên) với yêu cầu, xây dựng các hàm sau:
- Nhập, xuất phân số
- Hàm rút gọn.

Viết chương trình nhập vào N phân số, yêu cầu tìm xuất phân số nhỏ nhất (sau khi tối giản)

input:
- Dòng 1: số N
- N dòng tiếp theo, mỗi dòng gồm 2 số nguyên là tử và mẫu của 1 phân số

output:
Phân số nhỏ nhất (sau khi tối giản)

ví dụ:
input
2
1 2
2 4

output:
1/2
*/

#include <iostream>
#include <algorithm>
using namespace std;

int gcd(int a, int b){
    while(b != 0){
        int t = a % b;
        a = b;
        b = t;
    }
    return a;
}
struct PhanSo{
    int tu, mau;
    friend istream& operator>> (istream& in, PhanSo& ps){
        in >> ps.tu >> ps.mau;
        return in;
    }
    friend ostream& operator<< (ostream& out, const PhanSo& ps){
        out << ps.tu << "/" << ps.mau;
        return out;
    }
    void RutGon(){
        int ucln = gcd(tu, mau);
        tu /= ucln;
        mau /= ucln;
    }
    bool operator< (const PhanSo& other) const {
        return tu* other.mau < other.tu * mau;
    }
};

int main(){
    int n;
    cin >> n;
    PhanSo ps, min_ps;
    bool first = true;
    for(int i = 0; i < n; i++){
        cin >> ps;
        ps.RutGon();
        if(first || ps < min_ps) {
            min_ps = ps;
            first = false;
        }
    }
    cout << min_ps;
    return 0;
}