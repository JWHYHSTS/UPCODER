#include <iostream>
#include <bits/stdc++.h>
using namespace std;

#define nt int
#define nhap cin
#define xuat cout
#define va &&
#define kt return 0

nt main(){
    nt n, t, m;
    nhap >> n >> t >> m;
    if (m >= 1900 && t >= 1 && t <= 12) {
        if(t == 1 || t == 3 || t == 5 || t == 7 || t == 8 || t == 10 || t == 12){
            if(n >= 1 va n <= 31){
                xuat << "YES";
            } else {
                xuat << "NO";
            }
        } else if(t == 4 || t == 6 || t == 9 || t == 11){
            if(n >= 1 va n <= 30){
                xuat << "YES";
            } else {
                xuat << "NO";
            }
        } else if(t == 2){
            bool namNhuan = (m % 400 == 0) || (m % 4 == 0 va m % 100 != 0);
            if(namNhuan){
                if(n >= 1 va n <= 29){
                    xuat << "YES";
                } else {
                    xuat << "NO";
                }
            } else {
                if(n >= 1 va n <= 28){
                    xuat << "YES";
                } else {
                    xuat << "NO";
                }
            }
        } else {
            xuat << "NO";
        }
    } else {
        cout << "NO";
    }
    kt;
}
/*
#include <iostream>
#define thang_max 12
#define nam_min 1900
using namespace std;

int main() {
    int ngay, thang, nam;
    cin >> ngay >> thang >> nam;
    int ngay_thang[] = {0,31,28,31,30,31,30,31,31,30,31,30,31};
    if (nam < nam_min || thang < 1 || thang > thang_max) {
        cout << "NO";
        return 0;
    }
    int nhuan = (nam % 400 == 0 || (nam % 4 == 0 && nam % 100 != 0));
    if (nhuan && thang == 2) ngay_thang[2] = 29;
    if (ngay >= 1 && ngay <= ngay_thang[thang]) cout << "YES";
    else cout << "NO";
    return 0;
}
*/