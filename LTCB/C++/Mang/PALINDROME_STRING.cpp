#include <iostream>
#include <cmath>
#include <string>
#include <algorithm>
#include <cctype>
using namespace std;

#define sn int
#define nhap cin
#define xuat cout
#define kt return 0

sn main(){
    string s;
    getline(nhap, s);

    // Chuyển tất cả ký tự thành chữ thường 
    transform(s.begin(), s.end(), s.begin(), ::tolower);

    // Loại bỏ tất cả ký tự không phải chữ cái
    s.erase(remove_if(s.begin(), s.end(), [] (char c) {
        return !isalpha(c);
    }), s.end());

    // Tạo bản sao và dùng reverse đảo ngược
    string t = s;
    reverse(t.begin(), t.end());

    xuat << (s == t ? "YES" : "NO");
    kt;
}