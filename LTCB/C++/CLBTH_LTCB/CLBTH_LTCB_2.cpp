/*
Cho số nguyên dương n, đếm số cách để chia n chiếc kẹo thành các phần bằng nhau (mà không phá vỡ hay làm hỏng chiếc kẹo nào).

Input:

Gồm một số nguyên dương n duy nhất.

Output:

In ra số cách chia n chiếc kẹo thành các phần bằng nhau.

Ví dụ:


Input
10
Output
4


Giải thích:

Với n = 10, các cách chia thỏa mãn là:

- Chia thành 1 phần gồm 10 chiếc kẹo.

- Chia thành 2 phần, mỗi phần gồm 5 chiếc kẹo.

- Chia thành 5 phần, mỗi phần gồm 2 chiếc kẹo.

- Chia thành 10 phần, mỗi phần gồm 1 chiếc kẹo.
*/
#include <iostream>
using namespace std;
int DemSoKeo(int n){
    int dem = 0;
    for(int i = 1; i <= n; i++){
        if(n % i == 0) dem++;
    }
    return dem;
}
int main(){
    int n;
    cin >> n;
    cout << DemSoKeo(n);
    return 0;
}