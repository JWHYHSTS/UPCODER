/*
xây dựng 1 cấu trúc Phân Số (gồm tử và mẫu là số nguyên) với yêu cầu, xây dựng các hàm sau:
- Nhập, xuất phân số
- Hàm rút gọn.

Viết chương trình nhập vào nhiều phân số, yêu cầu tìm phân số nhỏ nhất trong các phân số trên (sau khi tối giản)

input:
- Gồm nhiều dòng, mỗi dòng gồm 2 số nguyên là tử và mẫu của 1 phân số

output: phân số nhỏ nhất (sau khi rút gọn)

Ví dụ:

input
1 2
2 4
output
1/2

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
    
    friend istream& operator>> (istream& in, PhanSo& ps){
        in >> ps.tu >> ps.mau;
        return in;
    }
    
    friend ostream& operator<< (ostream& out, const PhanSo& ps){
        out << ps.tu << "/" << ps.mau;
        return out;
    }
    
    void RutGon(){
        if(mau == 0) return;
        
        int ucln = gcd(tu, mau);
        tu /= ucln;
        mau /= ucln;

        if(mau < 0){
            tu = -tu;
            mau = -mau;
        }
    }
    
    bool operator< (const PhanSo& other) const {
        return tu * other.mau < other.tu * mau;
    }
};

void ps(){
    PhanSo ps, min_ps;
    bool first = true;
    for(int i = 0; i < 100; i++){
        cin >> ps;
        ps.RutGon();
        if(first || ps < min_ps) {
            min_ps = ps;
            first = false;
        }
    }
    cout << min_ps;
}
int main(){
    ps();
    return 0;
}