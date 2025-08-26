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
        friend PS operator+ (const PS& p1, const PS&p2){
            PS kq;
            kq.tu = p1.tu * p2.mau + p2.tu * p1.mau;
            kq.mau = p1.mau * p2.mau;
            sn ucln = __gcd(kq.tu, kq.mau);
            kq.tu /= ucln;
            kq.mau /= ucln;
            return kq;
        }
    };

   void cauPS(){
        sn n;
        nhap >> n;
        PS p;
        PS min_ps;
        bool fist = true;
        for(sn i = 0; i < n; i++){
            nhap >> p;
            p.TGPS();
            if(fist || p < min_ps){
                min_ps = p;
                fist = false;
            }
        }
        xuat << min_ps;
    }
    void cauPS3(){
        PS tong;
        PS p;
        while(nhap >> p){
            tong = tong + p;
        }
        tong.TGPS();
        xuat << tong;
    }
    sn main(){
        // cauPS();
        cauPS3();
        kt;
    }