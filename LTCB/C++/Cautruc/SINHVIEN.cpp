#include <iostream>
using namespace std;

#define sn int
#define nhap cin 
#define xuat cout 
#define kt return 0

struct SinhVien {
    string HoTen;
    sn NamSinh;
    double DTB;
    friend istream& operator>> (istream& in, SinhVien& SV){
        in >> SV.HoTen >> SV.NamSinh >> SV.DTB;
        return in;
    }
    friend ostream& operator<< (ostream& out, const SinhVien& SV){
        out << SV.HoTen << " " << SV.NamSinh << " " << SV.DTB;
        return out;
    }
};

sn main(){
    SinhVien ds[1000];
    sn n = 0;
    while(nhap >> ds[n]){
        n++;
    }
    if(n == 0){
        kt;
    }
    double maxDTB = ds[0].DTB;
    double minDTB = ds[0].DTB;
    for(sn i = 1; i < n; i++){ // Bắt đầu từ 1 vì đã gán maxDTB và minDTB từ phần tử đầu tiên
        if(ds[i].DTB > maxDTB){
            maxDTB = ds[i].DTB;
        }
        if(ds[i].DTB < minDTB){
            minDTB = ds[i].DTB;
        }
    }
    xuat << "Diem cao nhat lop:" << endl;
    sn dem = 1;
    for(sn i = 0; i < n; i++){ // Bắt đầu từ 0 vì cần kiểm tra tất cả phần tử
        if(ds[i].DTB == maxDTB){
            xuat <<"#"<< dem << endl;
            xuat << ds[i] << endl;
            dem++;
        }
    }
    xuat << "Diem thap nhat lop:" << endl;
    dem = 1;
    for(sn i = 0; i < n; i++){
        if(ds[i].DTB == minDTB){
            xuat <<"#"<< dem << endl;
            xuat << ds[i] << endl;
            dem++;
        }
    }
    kt;
}