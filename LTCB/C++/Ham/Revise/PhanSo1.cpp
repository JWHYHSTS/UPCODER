/*
Một phân số gồm tử  và mẫu (tử và mẫu là 2 số nguyên lớn hơn bằng 0 và bé hơn 100).
Yêu cầu viết chương trình nhập vào 2 phân số, yêu cầu xuất phân số tổng của 2 phân số đó (phân số tổng được rút gọn, sau đó xuất ra màn hình)

Nếu input có phân số nào có mẫu bằng 0 thì xuất kết quả ra -1

Dữ liệu đầu vào: gồm 2 dòng, mỗi dòng gồm 2 số nguyên cách nhau tối thiểu 1 khoảng trắng.

Dữ liệu đầu ra: gồm 1 dòng duy nhất chứa phân số tổng (sau khi rút gọn) của 2 phân số ban đầu, xuất theo dạng: tửsố/mẫusố

Ví dụ 1:

Input	Output
1 2     5/6
1 3



Ví dụ 2:

Input	Output
1 2     -1
1 0

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

void ps(){
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
void ps1(){
    PhanSo ps, tong;
    bool gtri = false;
    while(cin >> ps){
        if(ps.mau == 0){
            gtri = true;
            break;
        }
        tong = tong + ps;
    }
    if(gtri) cout << -1; // Nếu dòng lệnh if(ps.mau == 0) được thực thi, tức là có phân số có mẫu bằng 0 thì sẽ xuất -1
    else {
        tong.RutGon();
        cout << tong;
    }
}
int main(){
    //ps();
    //ps2();
    ps1();
    return 0;
}