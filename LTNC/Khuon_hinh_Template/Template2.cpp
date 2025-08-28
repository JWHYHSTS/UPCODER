#include <bits/stdc++.h>
using namespace std;

using ll = long long;

ll llgcd(ll a, ll b) {
    if (a < 0) a = -a;
    if (b < 0) b = -b;
    if (b == 0) return a;
    while (b) {
        ll t = a % b;
        a = b;
        b = t;
    }
    return a;
}

struct Fraction {
    ll p, q; // p/q
    Fraction(ll _p = 0, ll _q = 1) : p(_p), q(_q) {
        normalize();
    }
    void normalize() {
        if (q == 0) { p = 0; return; }
        if (q < 0) { p = -p; q = -q; }
        ll g = llgcd(p, q);
        if (g == 0) { q = 1; return; }
        p /= g; q /= g;
    }
    Fraction operator+(const Fraction& other) const {
        ll np = p * other.q + other.p * q;
        ll nq = q * other.q;
        return Fraction(np, nq);
    }
};

template<typename T>
struct Sequence {
    vector<T> a;
    void push(const T& x) { a.push_back(x); }
    T sum() const {
        if (a.empty()) return T();
        T s = a[0];
        for (size_t i = 1; i < a.size(); ++i) s = s + a[i];
        return s;
    }
};


int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    char type;
    if (!(cin >> type)) return 0;
    if (type == 'a') {
        Sequence<int> seq;
        int x;
        while (cin >> x) seq.push(x);
        int s = seq.sum();
        cout << s;
    } else if (type == 'b') {
        Sequence<Fraction> seq;
        ll p, q;
        while (cin >> p >> q) {
            seq.push(Fraction(p, q));
        }
        Fraction s = seq.sum();
        s.normalize();
        cout << s.p << "/" << s.q;
    }
    return 0;
}