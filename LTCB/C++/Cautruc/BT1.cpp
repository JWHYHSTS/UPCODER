// Phân Số 
#include <iostream>
#include <bits/stdc++.h>
using namespace std;

#define sn int
#define ll long long
#define nhap cin
#define xuat cout
#define kt return 0

sn gcd(sn a, sn b){
    while (b != 0) {
        sn t = a % b;
        a = b;
        b = t;
    }
    return a;
}

struct PS {
    ll tu, mau;
    // Nhập và xuất phân số
    PS(): tu(0), mau(1) {} // Constructor mặc định
    friend istream& operator>> (istream& in, PS& p){
        in >> p.tu >> p.mau;
        return in;
    }
    friend ostream& operator<< (ostream& out, const PS& p){
        out << p.tu << "/" << p.mau;
        return out;
    }
    // Tối giản phân số
    void TGPS() {
        sn ucln = gcd(tu, mau);
        tu /= ucln;
        mau /= ucln;
    }
    // Hàm tính tổng 2 phân số
    friend PS operator+ (const PS& p1, const PS& p2){
        PS kq;
        kq.tu = p1.tu * p2.mau + p2.tu * p1.mau;
        kq.mau = p1.mau * p2.mau;
        sn ucln = gcd(kq.tu, kq.mau);
        kq.tu /= ucln;
        kq.mau /= ucln;
        return kq;
    }
    // Hàm tính hiệu 2 phân số
    friend PS operator- (const PS& p1, const PS& p2){
        PS kq;
        kq.tu = p1.tu * p2.mau - p2.tu * p1.mau;
        kq.mau = p1.mau * p2.mau;
        sn ucln = gcd(kq.tu, kq.mau);
        kq.tu /= ucln;
        kq.mau /= ucln;
        return kq;
    }
    // Hàm tính tích 2 phân số
    friend PS operator* (const PS& p1, const PS& p2){
        PS kq;
        kq.tu = p1.tu * p2.tu;
        kq.mau = p1.mau * p2.mau;
        sn ucln = gcd (kq.tu, kq.mau);
        kq.tu /= ucln;
        kq.mau /= ucln;
        return kq;
    }
    // Hàm tính thương 2 phân số
    friend PS operator/ (const PS& p1, const PS& p2){
        if(p2.tu == 0) {
            throw runtime_error("Cannot divide by zero");
        }
        PS kq;
        kq.tu = p1.tu * p2.mau;
        kq.mau = p1.mau * p2.tu;
        sn ucln = gcd(kq.tu, kq.mau);
        kq.tu /= ucln;
        kq.mau /= ucln;
        return kq;
    }
    // Hàm so sánh 2 phân số
    friend bool operator< (const PS& p1, const PS& p2){
        return p1.tu * p2.mau < p2.tu * p1.mau;
    }
    friend bool operator> (const PS& p1, const PS& p2){
        return p1.tu * p2.mau > p2.tu * p1.mau;
    }
    friend bool operator== (const PS& p1, const PS& p2){
        return p1.tu * p2.mau == p2.tu * p1.mau;
    }

};

void b1(){
    PS p1;
    nhap >> p1;
    p1.TGPS();
    xuat << p1;
}

void b2(){
    PS p1, p2;
    nhap >> p1 >> p2;
    PS kq1 = p1 + p2;
    kq1.TGPS();
    xuat << kq1 << endl;
    PS kq2 = p1 - p2;
    kq2.TGPS();
    xuat << kq2 << endl;
    PS kq3 = p1 * p2;
    kq3.TGPS();
    xuat << kq3 << endl; 
    PS kq4 = p1/p2;
    kq4.TGPS();
    xuat << kq4 << endl;
    if(p1 > p2){
        xuat << p1 << " > " << p2 << endl;
    } else if(p1 < p2){
        xuat << p1 << " < " << p2 << endl;
    } else {
        xuat << p1 << " = " << p2 << endl;
    }
}

sn main(){
    //b1();
    b2();
    kt;
}