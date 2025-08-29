#include <iostream>
#include <vector>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n;
    if (!(cin >> n)) return 0;
    if (n < 0) return 0;
    int *a = nullptr;
    if (n > 0) a = new int[n];
    for (int i = 0; i < n; ++i) cin >> *(a + i);
    vector<pair<int,int>> mismatches;
    int *left = a;
    int *right = a + n - 1;
    while (left < right) {
        if (*left != *right) mismatches.emplace_back(*left, *right);
        ++left;
        --right;
    }
    if (mismatches.empty()) {
        cout << "mang doi xung";
    } else {
        cout << "mang khong doi xung\n";
        for (auto &p : mismatches) cout << p.first << ' ' << p.second << "\n";
    }
    delete[] a;
    return 0;
}