#include <iostream>
using namespace std;

int n;
string str;

int factorial(int n) {
    if (n < 1) return 1;
    return n * factorial(n - 1);
}

void chuoiHoanVi(string cur) {
    if ((int)cur.length() == n) {
        cout << cur << '\n';
        return;
    }
    for (int i = 1; i <= n; ++i) {
        string number = to_string(i);
        if (cur.find(number) != string::npos) continue;
        chuoiHoanVi(cur + number);
    }
}

int main() {
    if(!(cin >> n)) return 0;
    cout << factorial(n) << '\n';
    chuoiHoanVi("");
    return 0;
}