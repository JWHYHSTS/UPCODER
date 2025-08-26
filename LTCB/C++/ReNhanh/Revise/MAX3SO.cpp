/*
Nhập vào 3 sô nguyên a,b,c. Tìm sô lớn nhât và sô nhỏ nhất trong 3 sô đó.

Ví dụ:
input
1 2 3

outpt:
3 1
*/

#include <iostream>
using namespace std;
int main(){
    int a, b, c;
    cin >> a >> b >> c;
    int max_n = a, min_n = a;
    if(b > max_n) max_n = b;
    if(c > max_n) max_n = c;
    if(b < min_n) min_n = b;
    if(c < min_n) min_n = c;
    cout << max_n << " " << min_n << endl;
    return 0;
}