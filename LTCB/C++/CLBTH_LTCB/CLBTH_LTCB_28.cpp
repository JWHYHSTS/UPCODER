/*
Số “tương lai” là số có các ước (không kể 1 và chính nó) là các số nguyên tố. VD: số 10 có ước là 2 và 5 là các số nguyên tố nên 10 là số “tương lai”.
Cho dãy số nguyên a1, a2, ..., an. Hãy cho biết trong dãy trên có bao nhiêu số tương lai.

Input:

Dòng thứ nhất chứa số nguyên dương n.

Dòng thứ hai chứa n số nguyên a1, a2, ..., an.

Output:

Một số nguyên dương là số lượng các số tương lai.

Ví dụ:


Input
9
9 7 10 6 17 4 19 21 13

Output
5 

// Giải thích lý do tại sao đầu vào là 9 7 10 6 17 4 19 21 13 và đầu ra là 5:
// Trong dãy số này, các số tương lai là: 10 (có ước là 2 và 5), 6 (có ước là 2 và 3), 4 (có ước là 2), 21 (có ước là 3 và 7) và 19 (có ước là chính nó, nhưng không tính vào số tương lai vì không có ước khác ngoài chính nó).
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
int STL(int n){
    if(n <= 2) return 0;
    bool ktra = false;
    for(int i = 2; i <= n / 2; i++){
        if(n % i == 0){
            ktra = true;
            if(!SNT(i)) return 0;
        }
    }
    return ktra ? 1 : 0; // Trả về 1 nếu có ít nhất một ước là SNT, ngược lại trả về 0
}

int main(){
    int n;
    cin >> n;
    int a[n];
    for(int i = 0; i< n; i++){
        cin >> a[i];
    }
    int dem = 0;
    for(int i = 0; i < n; i++){
        if(STL(a[i])) dem++;
    }
    cout << dem;
    return 0;
}