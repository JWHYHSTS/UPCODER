/*#include <iostream>
#include <cmath>
using namespace std;

#define sn int
#define nhap cin
#define xuat cout
#define kt return 0

bool snt(sn n){
    if(n<2) return false;
    for(sn i = 2; i <= sqrt(n); i++){
        if(n % i == 0) return false;
    }
    return true;
}

sn main(){
    sn n;
    while(nhap >> n){
        sn tong = 0;
        for(; n != 0; n /= 10){
            sn temp = n % 10;
            if(snt(temp)) tong += temp;
        }
        xuat << tong << endl; 
    } 
    kt;
}
*/

/*
#include <iostream>
using namespace std;

// Hàm kiểm tra một chữ số có phải là số nguyên tố không
bool laChuSoNguyenTo(int d) {
    return d == 2 || d == 3 || d == 5 || d == 7;
}

int main() {
    int n;
    while (cin >> n) {
        int sum = 0, temp = n;
        while (temp != 0) {
            int d = temp % 10;
            if (laChuSoNguyenTo(d))
                sum += d;
            temp /= 10;
        }
        cout << sum << endl;
    }
    return 0;
}
*/

#include <iostream>
#include <cmath>
using namespace std;
int SNT(int n){
    if(n < 2) return 0;
    for(int i = 2; i <= sqrt(n); i++){
        if(n % i == 0) return 0;
    }
    return 1;
}

int tongcsnt(int n){
    int sum = 0;
    while(n != 0){
        int temp = n % 10;
        if(SNT(temp)) sum += temp;
        n /= 10;
    }
}
int main(){
    int n;
    while(cin >> n){
        cout << tongcsnt(n) << endl;
    }
    return 0;
}