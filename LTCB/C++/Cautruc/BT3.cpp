// Cấu trúc điểm của Thí sinh
#include <iostream>
#include <bits/stdc++.h>
using namespace std;

#define sn int
#define ll long long
#define st double
#define nhap cin
#define xuat cout
#define kt return 0

struct TS{
    string hoten;
    string ngaysinh;
    string lop;
    double diem1, diem2, diem3;

    // Chuẩn hóa ngày sinh về dd/mm/yyyy
    void chuanhoa_ngaysinh() {
        if (ngaysinh[1] == '/') ngaysinh = "0" + ngaysinh;
        if (ngaysinh[4] == '/') ngaysinh.insert(3, "0");
    }

    friend istream& operator>> (istream& in, TS& t){
        getline(in, t.hoten);
        in >> t.ngaysinh >> t.diem1 >> t.diem2 >> t.diem3;
        t.chuanhoa_ngaysinh();
        t.lop = "49SPTIN"; // Gán mặc định
        in.ignore(); // Bỏ ký tự xuống dòng cuối cùng để chuẩn bị cho lần nhập tiếp theo
        return in;
    }
    friend ostream& operator<< (ostream& out, const TS& t){
        out << t.hoten << " " << t.ngaysinh << " " << t.lop << " " << fixed << setprecision(1) << t.diem1 + t.diem2 + t.diem3 << endl;
        return out;
    }
};

void t1(){
    TS t;
    nhap >> t;
    xuat << t;
}

void t2(){
    sn n;
    nhap >> n;
    nhap.ignore(); // Bỏ ký tự xuống dòng sau khi nhập n
    TS ds[n];
    for(sn i = 0; i < n; i++){
        nhap >> ds[i];
    }
    sort(ds, ds + n, [](const TS& a, const TS& b) {
        double suma = a.diem1 + a.diem2 + a.diem3;
        double sumb = b.diem1 + b.diem2 + b.diem3;
        if (suma != sumb) return suma > sumb;
        return a.hoten < b.hoten;
    });
    xuat << "Danh sach thi sinh:\n";
    for(sn i = 0; i < n; i++){
        xuat << ds[i];
    }
}

sn main(){
    t1();
    //t2();
    kt;
}