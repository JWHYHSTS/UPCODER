/*
Input:
- Dòng 1: Nhập vào N là số lượng phần tử của mảng
- Dòng 2: N số nguyên (mỗi số cách 1 khoảng trắng)

Ouput:
Yêu cầu xuất tổng các số chính phương ra màn hình

ví dụ:
input:
4
1 2 3 4

output

*/
#include <iostream>
#include <cmath>
using namespace std;

int scp(int n)
{
    int x = sqrt(n);
    return (x * x == n) ? 1 : 0;
}
int snt(int n)
{
    if (n < 2)
        return 0;
    for (int i = 2; i <= sqrt(n); i++)
    {
        if (n % i == 0)
            return 0;
    }
    return 1;
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
    for (int i = 0; i < n; i++)
    {
        if (scp(a[i]))
            cout << a[i] << " ";
    }
    cout << endl;
    for (int i = 0; i < n; i++)
    {
        if (snt(a[i]))
            cout << a[i] << " ";
    }
    return 0;
}