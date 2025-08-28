#include <bits/stdc++.h>
using namespace std;

struct M1C {
    vector<int> a;
    void nhap() {
        int x;
        while (cin >> x) a.push_back(x);
    }
    void xuat() {
        for (size_t i = 0; i < a.size(); ++i) {
            if (i) cout << " ";
            cout << a[i];
        }
        cout << "\n";
    }
    int tong() {
        long long s = 0;
        for (int v : a) s += v;
        return static_cast<int>(s);
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    M1C m;
    m.nhap();
    cout << m.tong();
    return 0;
}