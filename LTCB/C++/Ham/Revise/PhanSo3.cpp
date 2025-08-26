/*
xây dựng 1 cấu trúc Phân Số (gồm tử và mẫu là số nguyên) với yêu cầu, xây dựng các hàm sau:
- Nhập, xuất phân số
- Hàm rút gọn.

Viết chương trình nhập vào dãy phân số, yêu cầu tính tổng của các phân số trên (sau khi tối giản)

input:
Gồm nhiều dòng, mỗi dòng gồm 2 số nguyên là tử và mẫu của 1 phân số

output: phân số tổng sau khi rút gọn

Ví dụ:

input
1 2
2 4
output
1/1 
*/

#include <iostream>
#include <algorithm>
using namespace std;

int gcd(int a, int b){
    a = abs(a);
    b = abs(b);
    while(b != 0){
        int t = a % b;
        a = b;
        b = t;
    }
    return a;
}
struct PhanSo{
    int tu, mau;
    PhanSo(): tu(0), mau(1) {}
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
    double giatri() const {
        return static_cast<double>(tu) / mau;
    }
    PhanSo operator+ (const PhanSo& other) const {
        PhanSo kq;
        kq.tu = tu * other.mau + other.tu * mau;
        kq.mau = mau * other.mau;
        kq.RutGon();
        return kq;
    }
};

void ps1(){
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
}
void ps2(){
    PhanSo ps;
    PhanSo tong;
    while(cin >> ps){
        ps.RutGon();
        tong = tong + ps;
    }
    tong.RutGon();
    cout  << tong;
}
int main(){
    // ps1();
    ps2();
    return 0;
}