#include <iostream>
#include <cmath>
using namespace std;

#define sn int
#define nhap cin 
#define xuat cout 
#define kt return 0

struct PhanSo {
    sn tu, mau;
    
    // Hàm nhập phân số
    void nhapps() {
        nhap >> tu >> mau;
    }
    
    // Hàm tính UCLN
    sn ucln(sn a, sn b) {
        if (b == 0) return a;
        return ucln(b, a % b);
    }
    
    // Hàm rút gọn phân số
    void rutGon() {
        if (mau == 0) return;
        sn uc = ucln(abs(tu), abs(mau));
        tu /= uc;
        mau /= uc;
        if (mau < 0) {
            tu = -tu;
            mau = -mau;
        }
    }
    
    // Hàm xuất phân số - ĐÃ SỬA
    void xuatps() {
        if (tu == 0) {
            xuat << "0";           // Nếu tử = 0, chỉ xuất "0"
        } else {
            xuat << tu << "/" << mau;  // Luôn xuất "tử/mẫu"
        }
    }
    
    // Phép cộng
    PhanSo cong(PhanSo other) {
        PhanSo kq;
        kq.tu = tu * other.mau + other.tu * mau;
        kq.mau = mau * other.mau;
        kq.rutGon();
        return kq;
    }
    
    // Phép trừ
    PhanSo tru(PhanSo other) {
        PhanSo kq;
        kq.tu = tu * other.mau - other.tu * mau;
        kq.mau = mau * other.mau;
        kq.rutGon();
        return kq;
    }
    
    // Phép nhân
    PhanSo nhan(PhanSo other) {
        PhanSo kq;
        kq.tu = tu * other.tu;
        kq.mau = mau * other.mau;
        kq.rutGon();
        return kq;
    }
    
    // Phép chia
    PhanSo chia(PhanSo other) {
        PhanSo kq;
        if (other.tu == 0) {
            kq.tu = 0; 
            kq.mau = 1; 
            return kq;
        }
        kq.tu = tu * other.mau;
        kq.mau = mau * other.tu;
        kq.rutGon();
        return kq;
    }
    
    // Kiểm tra phân số có bằng 0 không
    bool bangKhong() {
        return tu == 0;
    }
};

sn main() {
    PhanSo a, b;
    a.nhapps();
    b.nhapps();
    
    if (a.mau == 0 || b.mau == 0) {
        xuat << "-1" << endl;
        kt;
    }
    
    a.rutGon();
    b.rutGon();
    
    PhanSo tong = a.cong(b);
    tong.xuatps();
    xuat << endl;
    
    PhanSo hieu = a.tru(b);
    hieu.xuatps();
    xuat << endl;
    
    PhanSo tich = a.nhan(b);
    tich.xuatps();
    xuat << endl;
    
    if (!b.bangKhong()) {
        PhanSo thuong = a.chia(b);
        thuong.xuatps();
        xuat << endl;
    }
    
    kt;
}