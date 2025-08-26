#include <bits/stdc++.h>
using namespace std;

struct SoMoi {
    int A;
    SoMoi(int v = 0) : A(v) {}
    int sumDigits() const {
        int n = A < 0 ? -A : A;
        int s = 0;
        if (n == 0) return 0;
        while (n) { s += n % 10; n /= 10; }
        return s;
    }
    bool operator>(const SoMoi& other) const {
        return sumDigits() > other.sumDigits();
    }
    SoMoi operator+(const SoMoi& other) const {
        return SoMoi(sumDigits() + other.sumDigits());
    }
};

ostream& operator<<(ostream& os, const SoMoi& s) {
    os << "[SoMoi] " << s.A;
    return os;
}

istream& operator>>(istream& is, SoMoi& s) {
    is >> s.A;
    return is;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    SoMoi s1, s2;
    if (!(cin >> s1)) return 0;
    if (!(cin >> s2)) return 0;
    cout << s1 << "\n";
    cout << s2 << "\n";
    cout << (s1 > s2 ? "true" : "false") << "\n";
    cout << (s1 + s2) << "\n";
    return 0;
}