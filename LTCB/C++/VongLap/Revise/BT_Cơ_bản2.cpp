/*
Cho 2 số nguyên dương a, b < 100, viết hàm tìm UCLN và BCNN.

VD Input: 9 12
Output: 3 36 

*/

#include <iostream>
using namespace std;

int ucln(int a, int b){
    while(b != 0){
        int temp = a % b;
        a = b;
        b = temp;
    }
    return a;
}

int bcnn(int a, int b){
    return (a * b) / ucln(a,b);
}

int main(){
    int a, b;
    cin >> a >> b;
    cout << ucln(a, b) << " " << bcnn(a, b);
    return 0;
}