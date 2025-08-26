/*
Cho hai số nguyên dương a và b (a < b, a và b không vượt quá 1000). Hãy liệt kê tất cả các số nguyên trong đoạn [a, b] nếu tổng các chữ số của số nguyên đó là số nguyên tố. 
Ví dụ:

Input
10 15
Output
11 12 14 




Giải thích: Trong đoạn từ 10 đến 15 ta có
10 => 1 + 0 = 1 => 1 không phải số nguyên tố.
11 => 1 + 1 = 2 => 2 là số nguyên tố.
12 => 1 + 2 = 3 => 3 là số nguyên tố.
13 => 1 + 3 = 4 => 4 không phải số nguyên tố.
14 => 1 + 4 = 5 => 5 là số nguyên tố.
15 => 1 + 5 = 6 => 6 không phải số nguyên tố.


*/
#include <bits/stdc++.h>
using namespace std;
int SNT(int n){
    if (n < 2) return 0;
    for (int i = 2; i <= sqrt(n); ++i) {
        if (n % i == 0) return 0;
    }
    return 1;
}

int tongchuso(int n){
    int tong = 0;
    while(n > 0){
        tong += n % 10;
        n /= 10;
    }
    return tong;
}

int main(){
    int a, b;
    cin >> a >> b;
    for(int i = a; i <= b; i++){
        if(SNT(tongchuso(i))) cout << i << " ";
    }
    return 0;
}