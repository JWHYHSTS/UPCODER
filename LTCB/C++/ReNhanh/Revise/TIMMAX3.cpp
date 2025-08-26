/*
Input: 5 số nguyên a, b, c ,d, e (đều bé hơn 10^5)

Output: xuất ra số có giá trị nhất lớn trong 5 số trong Input

Ví dụ:

Input	
1 2 3 4 5
Output
5
*/
#include <iostream>
#include <algorithm>
using namespace std;
int main(){
    int a,b,c,d,e;
    cin >> a >> b >> c >> d >> e;
    cout << max({a,b,c,d,e});
    return 0;
}