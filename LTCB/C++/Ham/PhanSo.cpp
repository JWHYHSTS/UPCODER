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
            sn ucln = __gcd(tu, mau);
            tu /= ucln;
            mau /= ucln;
        }
        bool operator<(const PS& other) const {
            return tu * other.mau < other.tu * mau;
        }
    };

    sn main(){
        sn n;
        nhap >> n;
        PS p;
        PS min_ps;
        bool fist = true; // Biến để kiểm tra phần tử đầu tiên và đặt cho giá trị là true
        for(sn i = 0; i < n; i++){
            nhap >> p;
            p.TGPS();
            if(fist || p < min_ps){ // So sánh với phần tử đầu tiên 
                min_ps = p;
                fist = false; // Đặt biến fist thành false sau khi đã tìm được phần tử đầu tiên
            }
        }
        xuat << min_ps;
        kt;
    }