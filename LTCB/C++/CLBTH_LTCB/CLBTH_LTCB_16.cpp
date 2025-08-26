/*
Cho số nguyên dương k, hãy liệt kê tất cả các số nguyên tố từ 1 đến k.

Input:

Gồm một số nguyên dương k duy nhất. (1 < k < 105).

Output:

Gồm nhiều dòng, mỗi dòng lần lượt chứa một số nguyên tố trong đoạn [1, k]. Các số được in theo thứ tự từ bé đến lớn.

Ví dụ:


Input
3
Output
2
3

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
int main(){
    int n;
    cin >> n;
    for(int i = 0; i <= n; i++){
        if(SNT(i)) cout << i << endl;
    }
    return 0;
}