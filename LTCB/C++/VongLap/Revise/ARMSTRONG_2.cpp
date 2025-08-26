/*
Armstrong Numbers 2

Một số nguyên dương có n chữ số được gọi là số Armstrong khi tổng các lũy thừa bậc n của các chữ số của nó bằng chính nó.

Ví dụ:

371 là số Armstrong vì: 3^3 + 7^3 + 1^3 = 371
8208 là số Armstrong vì: 8^4 + 2^4 + 8^4 = 8208


Hãy tìm tất cả các số Armstrong trong đoạn [A; B].



Input:

Gồm 2 số nguyên dương A, B cách nhau bởi 1 khoảng trắng (1 <= A <= B <= 10^7)

Output:

In ra tất cả các số Armstrong trong đoạn [A;B]. 

Xuất theo thứ tự từ nhỏ đến lớn, mỗi số cách nhau một khoảng trắng.

Nếu trong đoạn [A; B] không có số Armstrong nào thì xuất -1



Ví dụ:

Input	Output
30 40   -1
Ví dụ:

Input	Output
300 400 370 371



Ví dụ:

Input	    Output
8000 9000   8208

*/
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