/*
Vì một lí do đặc biệt gì đó, Tỷ đặc biệt thích số 3. Chính vì vậy, bạn được định nghĩa một số đẹp. Số đẹp là khi cộng các chữ số của nó lại với nhau thì ta được một chữ số có tận cùng là số 3.

Input:

Một số nguyên dương n (0 < n ≤ 1018).

Output:

Nếu n là số đẹp thì in ra “YES”, nếu không thì in ra “NO”.

Ví dụ:


Input
3
Output
YES

*/

#include <iostream>
using namespace std;
#define ll long long
int main(){
    ll n;
    cin >> n;
    ll tong = 0;
    while(n > 0){
        tong += n % 10;
        n /= 10;
    }
    if(tong % 10 == 3) cout << "YES";
    else cout << "NO";
    return 0;
}