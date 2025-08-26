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
#include <bits/stdc++.h>
using namespace std;

int UCLN(int a, int b){
    a = abs(a);
    b = abs(b);
    while(b != 0){
        int t = a % b;
        a = b;
        b = t;
    }
    return a;
}
struct PS{
    int tu, mau;
    PS(): tu(0), mau(1) {}
    friend istream& operator>> (istream& in, PS& p){
        in >> p.tu >> p.mau;
        return in;
    }
    friend ostream& operator<< (ostream& out, const PS& p){
        out << p.tu << "/" <<p.mau;
        return out;
    }
    void RG(){
        int ucln = UCLN(tu, mau);
        tu /= ucln;
        mau /= ucln;
    }
    bool operator< (const PS& other) const {
        return tu * other.mau < other.tu * mau;
    }
    PS operator+(const PS& other) const {
        PS kq;
        kq.tu = tu * other.mau + other.tu * mau;
        kq.mau = mau * other.mau;
        kq.RG();
        return kq;
    }
};

void PhanSo(){
    int n;
    cin >> n;
    PS p;
    PS min_ps;
    bool ktra = true;
    for(int i = 0; i < n; i++){ 
        cin >> p;
        p.RG();
        if(ktra || p < min_ps){
            min_ps = p;
            ktra = false;
        }
    }
    cout << min_ps;
}

void PhanSo3(){
    PS p;
    PS tong;
    while(cin >> p){
        p.RG();
        tong = tong + p;
    }
    cout << tong;
}
void PhanSo4(){
    PS p;
    PS min_ps;
    bool ktra = true;
    for(int i = 0; i < 100; i++){
        cin >> p;
        p.RG();
        if(ktra || p < min_ps){
            min_ps = p;
            ktra = false;
        }
    }
    cout << min_ps;
}
int main(){
    //PhanSo();
    //PhanSo3();
    PhanSo4();
    return 0;
}