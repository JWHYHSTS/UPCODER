#include <iostream>
#include <cmath>
using namespace std;

bool isPrime(int x) {
    if (x < 2) return false;
    if (x == 2 || x == 3) return true;
    if (x % 2 == 0 || x % 3 == 0) return false;
    for (int i = 5; 1LL * i * i <= x; i += 6) {
        if (x % i == 0 || x % (i + 2) == 0) return false;
    }
    return true;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int m, M;
    if (!(cin >> m >> M)) return 0;
    if (m > M) return 0;
    // Count primes
    int cnt = 0;
    for (int x = m; x <= M; ++x)
        if (isPrime(x)) ++cnt;
    if (cnt == 0) return 0;
    int *primes = new int[cnt];
    int *p = primes;
    for (int x = m; x <= M; ++x)
        if (isPrime(x)) {
            *p = x;
            ++p;
        }
    int *it = primes;
    for (int i = 0; i < cnt; ++i) {
        cout << *(it + i);
        if (i + 1 < cnt) cout << ' ';
    }
    delete[] primes;
    return 0;
}