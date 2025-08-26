/*
Tìm số tự nhiên có 3 chữ số, biết chữ số hàng chục thua hàng đơn vị 3 đơn vị và hàng đơn vị hơn hàng trăm 6 đơn vị. Nếu xen chữ số 0 vào giữa hàng đơn vị và hàng chục thì được số mới lớn hơn số đã cho 2250 đơn vị.

Input	Output

Số tìm được theo yêu cầu đề.
*/
#include <iostream>
using namespace std;

int main() {
    for (int a = 1; a <= 9; a++) {
        int c = a + 6;
        if (c > 9) continue;
        
        int b = c - 3;
        if (b < 0) continue;
        
        int original = 100 * a + 10 * b + c;      // abc
        int new_number = 1000 * a + 100 * b + c;  // ab0c (xen 0 vào giữa b và c)
        
        if (new_number - original == 2250) {
            cout << original;
            return 0;
        }
    }
    
    return 0;
}