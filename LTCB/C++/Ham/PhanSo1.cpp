#include <bits/stdc++.h>
using namespace std;

#define sn int
#define nhap cin
#define xuat cout
#define kt return 0

struct PS{
    sn tu, mau;
    PS(): tu(0), mau(1) {} 
    friend istream& operator>> (istream& in, PS& p){
        in >> p.tu >> p.mau;
        return in;
    }
    friend ostream& operator<<(ostream& out, const PS& p){
        out << p.tu << "/" << p.mau;
        return out;
    }
    void TGPS(){
        if(mau == 0) return;
        sn ucln = __gcd(abs(tu), abs(mau));
        tu /= ucln;
        mau /= ucln;
        if(mau < 0){
            tu = -tu;
            mau = -mau;
        }
    }
    bool giatri() const{
        return mau != 0;
    }
    friend PS operator+ (const PS& p1, const PS& p2){
        PS kq;
        kq.tu = p1.tu * p2.mau + p2.tu * p1.mau;
        kq.mau = p1.mau * p2.mau;
        kq.TGPS();
        return kq;
    }
};

sn main(){
    PS tong;
    PS p;
    bool gtri = false;
    while(nhap >> p){
        if(p.mau == 0){
            gtri = true;
            break; // Dừng khi gặp phân số có mẫu bằng 0
        }
        tong = tong + p;
    }
    if(gtri) xuat << -1; // Nếu if(gtri) là true, in -1 
    else {
    tong.TGPS();
    xuat << tong;
    }
    kt;
}