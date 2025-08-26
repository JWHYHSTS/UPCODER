/*
Yêu cầu 1:  Xây dựng cấu trúc ĐIỂM gồm tung độ và hoành độ (số nguyên)

-      Viết hàm nhập,xuất điểm (xem ví dụ đê hiểu rõ cách xuất hơn)

-      Viết hàm tính khoảng cách giữa 2 điểm

-      Viết hàm kiểm tra 2 điểm có trùng nhau không?

Yêu cầu 2: Xây dựng cấu trúc TAMGIAC gồm 3 điểm (PHẢI dựa vào cấu trúc ĐIỂM ở trên)

-      Viết quá tải hàm nhập,xuất (không cần kiểm tra điều kiện của tam giác, giả sử với 3 điểm bất kỳ đều là tam giác) (xem ví dụ đê hiểu rõ cách xuất hơn)

-      Viết hàm tính chu vi tam giác

-      Viết hàm so sánh chu vi của 2 tam giac.

-      Viết hàm kiểm tra 2 TAM GIÁC có trùng nhau hay không?

Yêu cầu 3: nhập dữ liệu tọa độ của 2 tam giác theo cấu trúc

-      Dòng 1: 3 điểm của tam giác 1

-      Dòng 2: 3 điểm của tam giác 2
Xuất kết quả theo cấu trúc sau:

-      Dòng 1: xuất các tọa độ của tam giác 1

-      Dòng 2: xuất các tọa độ của tam giác 2

-      Dòng 1: ghi TRUE, nếu tam giác 1 có chu vi < chu vi của tam giác 2, ngược lại ghi FALSE

-      Dòng 2: ghi TRUE, nếu 2 tam giác trùng nhau, ngược lại ghi FALSE


Ví dụ:

Input:
1 2 3 4 5 6
7 8 9 0 1 2

 

Output:
(1,2)(3,4)(5,6)
(7,8)(9,0)(1,2)
TRUE
FALSE.*/

#include <iostream>
#include <cmath>
using namespace std;

#define sn int
#define nhap cin
#define cautruc struct
#define xuat cout
#define kt return 0

cautruc Diem {
    sn x, y;
    // Ham nhap & xuat diem
    friend istream& operator>> (istream& in, Diem& d){
        in >> d.x >> d.y;
        return in;
    }
    friend ostream& operator<< (ostream& out, const Diem& d){
        out << "(" << d.x <<","<<d.y << ")";
        return out;
    }
    // Ham tinh khoang cach giua 2 diem
    double khoangCach(const Diem& d) const {
        return sqrt(pow(x - d.x, 2) + pow(y - d.y, 2));
    }
    // Ham kiem tra 2 diem co trung nhau ko
    bool bn(const Diem& other) const {
        return (x == other.x && y == other.y);
    }
};

cautruc Tamgiac{
    Diem a,b,c;
    // Ham nhap & xuat tam giac
    friend istream& operator>> (istream& in, Tamgiac& t){
        in >> t.a >> t.b >> t.c;
        return in;
    }
    friend ostream& operator<< (ostream& out, const Tamgiac& t){
        out << t.a << t.b << t.c;
        return out;
    }
    // Ham tinh chu vi tam giac
    double chuvi()const {
        return a.khoangCach(b) + b.khoangCach(c) + c.khoangCach(a);
    }
    // Ham so sanh chu vi 2 tam giac
    bool chuviNhoHon(const Tamgiac& other) const {
        return chuvi() < other.chuvi();
    }
    // Ham kiem tra 2 tam giac co trung nhau ko
    bool bn(const Tamgiac& other) const {
        return (a.bn(other.a) && b.bn(other.b) && c.bn(other.c)) ||
           (a.bn(other.a) && b.bn(other.c) && c.bn(other.b)) ||
           (a.bn(other.b) && b.bn(other.a) && c.bn(other.c)) ||
           (a.bn(other.b) && b.bn(other.c) && c.bn(other.a)) ||
           (a.bn(other.c) && b.bn(other.a) && c.bn(other.b)) ||
           (a.bn(other.c) && b.bn(other.b) && c.bn(other.a));
    }
};

sn main(){
    Tamgiac t1, t2;
    nhap >> t1 >> t2;
    xuat << t1 << endl;
    xuat << t2 << endl;

    // So sanh chu vi
    if(t1.chuviNhoHon(t2)){
        xuat << "TRUE" << endl;
    } else xuat << "FALSE" << endl;

    // Kiem tra 2 tam giac co trung nhau
    if(t1.bn(t2)){
        xuat << "TRUE" << endl;
    }else xuat << "FALSE" << endl;
    kt;
}