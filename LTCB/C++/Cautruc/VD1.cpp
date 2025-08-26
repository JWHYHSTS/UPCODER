#include <bits/stdc++.h>
using namespace std;

#define sn int
#define nhap cin
#define xuat cout
#define kt return 0

struct SV{
    string mssv;
    string hoten;
    double gpa;
    string dc;
    // Constructor mặc định
    SV(){
        mssv = "4901";
        hoten = "Nguyen Van A";
        gpa = 3.5;
        dc = "123 Nguyen Trai";
    }
    // Constructor có tham số
    SV(string mssv, string hoten, double gpa, string dc){
        this->mssv = mssv;
        this->hoten = hoten;
        this->gpa = gpa;
        this->dc = dc;
    }

    void nhaps(){
        nhap >> mssv;
        nhap.ignore();
        getline(nhap, hoten);
        nhap >> gpa;
        nhap.ignore();
        getline(nhap, dc);
    }
    void xuats(){
        xuat << mssv << " " << hoten << " " << fixed << setprecision(2) << gpa << " " << dc << endl;
    }
    // Hàm so sánh GPA
    friend bool operator< (const SV& s1, const SV& s2){
        return s1.gpa < s2.gpa;
    }
};

sn main(){
    // Sử dụng struct SV
    // Có thể sử dụng constructor mặc định
    //SV a;
    //a.nhaps();
    //a.xuats();
    // Hoặc có thể sử dụng constructor có tham số
    //SV b("4901", "Nguyen Van A", 3.5, "123 Nguyen Trai");
    //b.xuats();

    // Sử dụng mảng struct SV
    sn n;
    nhap >> n;
    SV ds[n];
    for(sn i = 0; i < n; i++){
        ds[i].nhaps();
    }
    sort(ds,ds + n); // Sắp xếp theo GPA tăng dần
    for(SV x: ds){ // for(sn  i = 0; i < n; i++)
        x.xuats();
    }

    // SV a{"4901", "Nguyen Van A", 3.5, "123 Nguyen Trai"};
    //nhap >> a.mssv;
    //nhap.ignore(); // Ignore dùng để bỏ qua ký tự newline sau khi đọc mssv
    //getline(nhap, a.hoten);
    //nhap >> a.gpa;
    //nhap.ignore();
    //getline(nhap, a.dc);
    //xuat << a.mssv << " " << a.hoten << " " << fixed << setprecision(2) << a.gpa << " " << a.dc << endl;

    kt;
}

/*
VD Input:
2
1234
Nguyen Van B
3.2
12 Tran Phu
5678
Le Thi C
3.8
45 Le Loi
*/