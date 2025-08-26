#include <bits/stdc++.h>
using namespace std;

#define sn int
#define nhap cin 
#define xuat cout
#define kt return 0

struct sophuc {
    double a,b;
    friend istream& operator>> (istream& in, sophuc& s){
        in >> s.a >> s.b;
        return in;    
    }
    friend ostream& operator<< (ostream& out, const sophuc& s){
        out << fixed << setprecision(2) << s.a << " + " << s.b << "i";
        return out;
    }
    // Constructor mặc định
    sophuc() : a(0), b(0) {}
    // Constructor có tham số
    sophuc(double a, double b) : a(a), b(b) {}
    // Hàm cộng hai số phức 
    friend sophuc operator+ (const sophuc& s1, const sophuc& s2){
        return sophuc(s1.a + s2.a, s1.b + s2.b);
    }
    // Hàm trừ hai số phức
    friend sophuc operator- (const sophuc& s1, const sophuc& s2){
        return sophuc(s1.a - s2.a, s1.b - s2.b);
    }
    // Hàm nhân hai số phức
    friend sophuc operator* (const sophuc& s1, const sophuc& s2){
        return sophuc(s1.a * s2.a - s1.b * s2.b, s1.a * s2.b + s1.b * s2.a);
    }
    // Hàm chia hai số phức
    friend sophuc operator/ (const sophuc& s1, const sophuc& s2){
        double ms = s2.a * s2.a + s2.b * s2.b;
        if (ms == 0) {
            throw runtime_error("Cannot divide by zero");
        }
        return sophuc((s1.a * s2.a + s1.b * s2.b) / ms, (s1.b * s2.a - s1.a * s2.b) / ms);
    }
    friend bool operator== (const sophuc& s1, const sophuc& s2){
        return (s1.a == s2.a && s1.b == s2.b);
    }
    friend bool operator!= (const sophuc& s1, const sophuc& s2){
        return !(s1 == s2);
    }
    // Hàm so sánh hai số phức
    friend bool operator< (const sophuc& s1, const sophuc& s2){
        return (s1.a * s1.a + s1.b * s1.b < s2.a * s2.a + s2.b * s2.b);
    }
    friend bool operator> (const sophuc& s1, const sophuc& s2){
        return (s1.a * s1.a + s1.b * s1.b > s2.a * s2.a + s2.b * s2.b);
    }
};

sn main(){
    sophuc s1, s2;
    nhap >> s1 >> s2;
    sophuc s3 = s1 + s2;
    xuat << s3 << endl;
    sophuc s4 = s1 - s2;
    xuat << s4 << endl;
    sophuc s5 = s1 * s2;
    xuat << s5 << endl;
    sophuc s6 = s1 / s2;
    xuat << s6 << endl;

    if (s1 == s2) {
        xuat << "s1 == s2" << endl;
    } else {
        xuat << "s1 != s2" << endl;
    }
    if (s1 < s2) {
        xuat << "s1 < s2" << endl;
    } else if (s1 > s2) {
        xuat << "s1 > s2" << endl;
    } else {
        xuat << "s1 == s2" << endl;
    }

    kt;

}