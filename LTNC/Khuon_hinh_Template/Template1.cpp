#include <iostream>
using namespace std;

struct Fraction {
    int tu, mau;
    Fraction(int t = 0, int m = 1) : tu(t), mau(m) {}
};

bool operator>(const Fraction& a, const Fraction& b) {
    return a.tu * b.mau > b.tu * a.mau;
}

ostream& operator<<(ostream& os, const Fraction& f) {
    os << f.tu << "/" << f.mau;
    return os;
}

template <typename T>
T findMax(T a, T b, T c) {
    T res = a;
    if (b > res) res = b;
    if (c > res) res = c;
    return res;
}

int main() {
    char type;
    cin >> type;
    if (type == 'a') {
        int x, y, z;
        cin >> x >> y >> z;
        cout << findMax(x, y, z);
    } else if (type == 'b') {
        double x, y, z;
        cin >> x >> y >> z;
        cout << findMax(x, y, z);
    } else if (type == 'c') {
        Fraction x, y, z;
        cin >> x.tu >> x.mau;
        cin >> y.tu >> y.mau;
        cin >> z.tu >> z.mau;
        cout << findMax(x, y, z);
    }
    return 0;
}