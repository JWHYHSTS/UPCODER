// Cấu trúc điểm xy
#include <iostream>
#include <bits/stdc++.h>
using namespace std;

#define sn int
#define ll long long
#define st double
#define nhap cin
#define xuat cout
#define kt return 0

struct Point{
    st x,y;
    // Constructor mặc định
    Point(): x(0), y(0) {}
    // Constructor có tham số
    Point(st x, st y): x(x), y(y) {}
    // Nhập, xuât điểm
    friend istream& operator>> (istream& in, Point& p){
        in >> p.x >> p.y;
        return in;
    }
    friend ostream& operator<< (ostream& out, const Point& p){
        out << fixed << setprecision(2) << "(" << p.x << "," << p.y << ")";
        return out;
    }
    // Hàm tính khoảng cách giữa 2 điểm
    friend st distance(const Point& p1, const Point& p2){
        return sqrt(pow(p1.x - p2.x,2) + pow(p1.y - p2.y,2));
    }

};

sn main(){
    Point p1, p2;
    sn t;
    nhap >> t;
    while(t--){
        nhap >> p1 >> p2;
        xuat << p1 << " " << p2 << " ";
        st d = distance(p1,p2);
        xuat << fixed << setprecision(4) << d << endl;
    }
    kt;
}