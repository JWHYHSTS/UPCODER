#include <bits/stdc++.h>
using namespace std;

// Kieu SoMoi
class SoMoi {
    long long x; // gia tri goc (doi voi ket qua tong se luu luon tong cac digitSum)
    static long long digitSum(long long v) {
        if (v < 0) v = -v;
        long long s = 0;
        while (v) { s += v % 10; v /= 10; }
        return s;
    }
public:
    SoMoi(long long v = 0) : x(v) {}
    long long original() const { return x; }
    long long moi() const { return digitSum(x); }

    // Toan tu + (chi dung khi cong hai so rieng le, KHONG dung de cong tich luy nhieu lan)
    SoMoi operator+(const SoMoi& other) const {
        return SoMoi(this->moi() + other.moi());
    }
    bool operator>(const SoMoi& other) const { return x > other.x; }
    bool operator==(const SoMoi& other) const { return x == other.x; }

    friend istream& operator>>(istream& is, SoMoi& v) {
        long long t;
        if (is >> t) v.x = t;
        return is;
    }
    friend ostream& operator<<(ostream& os, const SoMoi& v) {
        os << "[SoMoi] " << v.x;
        return os;
    }
};

// Mang tong quat dung template
template <typename T>
struct Mang {
    vector<T> a;
    void push(const T& v) {
        if (a.size() < 1000) a.push_back(v);
    }
    size_t size() const { return a.size(); }
    const T& operator[](size_t i) const { return a[i]; }
};

// process cho kieu so nguyen
template <typename T>
void processNumber(const Mang<T>& m) {
    if (m.size() == 0) return;
    T mx = m[0];
    long long sum = 0;
    for (size_t i = 0; i < m.size(); ++i) {
        if (m[i] > mx) mx = m[i];
        sum += m[i];
    }
    int cnt = 0;
    for (size_t i = 0; i < m.size(); ++i)
        if (m[i] == mx) ++cnt;
    cout << mx << "\n" << cnt << "\n" << sum << "\n";
}

// Chuyen hoa chuyen biet cho SoMoi de tranh loi cong lap lai lam mat thong tin (test sai truoc)
void processSoMoi(const Mang<SoMoi>& m) {
    if (m.size() == 0) return;
    SoMoi mx = m[0];
    for (size_t i = 1; i < m.size(); ++i)
        if (m[i] > mx) mx = m[i];
    int cnt = 0;
    long long tongDigitSum = 0;
    for (size_t i = 0; i < m.size(); ++i) {
        if (m[i] == mx) ++cnt;
        tongDigitSum += m[i].moi(); // cong thang digitSum tung phan tu
    }
    cout << mx << "\n";
    cout << cnt << "\n";
    cout << SoMoi(tongDigitSum) << "\n"; // dinh dang [SoMoi] <value>
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    string type;
    if (!(cin >> type)) return 0;

    if (type == "N") {
        Mang<int> m;
        int val;
        while (cin >> val) m.push(val);
        processNumber(m);
    } else if (type == "M") {
        Mang<SoMoi> m;
        SoMoi v;
        while (cin >> v) m.push(v);
        processSoMoi(m);
    }
    return 0;
}