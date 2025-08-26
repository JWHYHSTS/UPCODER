/*
Input:
- Dòng 1: Nhập vào N là số lượng phần tử của mảng
- Dòng 2: N số nguyên (mỗi số cách 1 khoảng trắng)

Ouput:
- Dòng 1: xuất các số chính phương của dãy
- Dòng 2: xuất các số nguyên tố của dãy

Ví dụ:
input
4
1 2 3 4
output
1 4
2 3
*/
#include <iostream>
#include <cmath>
using namespace std;

int scp(int n)
{
    int x = sqrt(n);
    return (x * x == n) ? 1 : 0;
}

int main()
{
    int n;
    cin >> n;
    int a[100];
    for (int i = 0; i < n; i++)
    {
        cin >> a[i];
    }
    int tong = 0;
    for (int i = 0; i < n; i++)
    {
        if (scp(a[i]))
            tong += a[i];
    }
    cout << tong;
    return 0;
}