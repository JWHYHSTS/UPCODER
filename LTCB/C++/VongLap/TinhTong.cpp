#include <iostream>
#include <cmath>
using namespace std;

#define sn int
#define nhap cin
#define xuat cout
#define kt return 0

sn main(){
    sn n;
    while(nhap >> n) {
        int tong = 0;
        for(; n !=0; n /= 10){
            tong += n%10;
        }
        xuat << tong << endl;
    }
    kt;
}

/*
#include <iostream>
using namespace std;

int main() {
    int n;
    while (cin >> n) { // Nhập từng số cho đến khi kết thúc nhập 
        int sum = 0;
        while (n != 0) {
            sum += n % 10; // Cộng chữ số cuối cùng
            n /= 10;       // Bỏ chữ số cuối cùng
        }
        cout << sum << endl;
    }
    return 0;
}
*/
