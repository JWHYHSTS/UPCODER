#include <iostream>
using namespace std;

#define sn int
#define nhap cin
#define xuat cout
#define kt return 0

sn pow_table[10][8];

void init_pow_table() {
    for(sn d = 0; d <= 9; d++)
        for(sn k = 1; k <= 7; k++) {
            sn p = 1;
            for(sn i = 0; i < k; i++) p *= d;
            pow_table[d][k] = p;
        }
}

bool is_armstrong(sn n){
    sn tong = 0, m = n, dem = 0;
    if(n == 0) dem = 1;
    else {
        while(m > 0){
            m /= 10;
            dem++;
        }
    }
    m = n;
    if(n == 0) tong = 0;
    else {
        while(m > 0){
            sn cs = m % 10;
            tong += pow_table[cs][dem];
            m /= 10;
        }
    }
    if(n == 0) return (tong == n);
    return (tong == n);
}

sn main(){
    init_pow_table();
    sn a, b;
    nhap >> a >> b;
    bool found = false;
    for(sn i = a; i <= b; i++){
        if(is_armstrong(i)){
            if(found) xuat << " ";
            xuat << i;
            found = true;
        }
    }
    if(!found) xuat << -1;
    xuat << endl;
    kt;
}

    /*
#include <iostream>
using namespace std;

int main() {
    int a, b, sum, num, len;
    int n[10][9];
    bool check = true;

    for (int i = 0; i < 10; i++) {
        n[i][0] = 1;
        for (int j = 1; j <= 8; j++) 
            n[i][j] = n[i][j-1]*i;
    }

    cin >> a >> b;
    for (int i = a; i <= b; i++) {
        int tmp = i;
        sum = 0, len = 0, num = i;

        while (tmp > 0) 
            len++, tmp /= 10;
        
        tmp = i;
        while (tmp > 0) {
            sum += n[tmp % 10][len];
            tmp /= 10;
            if (sum > i) {
                i -= i % 10, i += 9;
                break;
            }
        }

        if (sum == num) {
            cout << i << ' ';
            check = false;
        } 
    }

    if (check) cout << -1;
    return 0;
}
    */