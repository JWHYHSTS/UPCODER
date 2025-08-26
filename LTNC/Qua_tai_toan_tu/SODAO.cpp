#include <bits/stdc++.h>
using namespace std;

struct SoDao {
    int n;
    SoDao(int v = 0) : n(v) {}
    int reverseValue() const {
        int a = n / 100;
        int b = (n / 10) % 10;
        int c = n % 10;
        return c * 100 + b * 10 + a;
    }
    bool operator>(const SoDao& other) const {
        return reverseValue() > other.reverseValue();
    }
    // SoDao + int -> int
    int operator+(int val) const {
        return reverseValue() + val;
    }
};

int operator+(int val, const SoDao& sd) {
    return val + sd.reverseValue();
}

ostream& operator<<(ostream& os, const SoDao& sd) {
    os << "[SoDao] " << sd.n;
    return os;
}

istream& operator>>(istream& is, SoDao& sd) {
    is >> sd.n;
    return is;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    SoDao s1, s2;
    if (!(cin >> s1)) return 0;
    if (!(cin >> s2)) return 0;
    cout << s1 << "\n";
    cout << s2 << "\n";
    cout << (s1 > s2 ? "YES" : "NO") << "\n";
    int total = (s1 + 0) + s2; // (reverse s1) + (reverse s2)
    cout << total << "\n";
    return 0;
}