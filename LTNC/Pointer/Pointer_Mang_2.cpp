#include <iostream>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n;
    if (!(cin >> n) || n <= 0) return 0;
    int *a = new int[n * n];
    for (int i = 0; i < n * n; ++i) a[i] = 0;
    for (int i = 0; i < n; ++i) a[i * n + i] = 1;
    for (int i = 0; i < n; ++i) {
        int *row = a + i * n;
        for (int j = 0; j < n; ++j) {
            cout << row[j];
            if (j + 1 < n) cout << ' ';
        }
        if (i + 1 < n) cout << "\n";
    }
    delete[] a;
    return 0;
}