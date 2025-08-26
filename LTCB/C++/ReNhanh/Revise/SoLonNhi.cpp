/*
Cho 4 số nguyên không âm a, b, c, d. Hãy tìm số lớn thứ nhì trong 4 số này.

Input:
4 số a, b, c, d. Mỗi số cách nhau 1 khoảng trắng. Giá trị mỗi số không vượt quá 100.
Output:
Số lớn thứ nhì trong 4 số này. Nếu không tồn tại số lớn thứ nhì thì xuất -1.

Ví dụ 1:

Input
2 5 3 1
Output
3
*/
#include <iostream>
using namespace std;
int main(){
    int a,b,c,d;
    cin >> a >> b >> c >> d;
    int max1 = a;
    int max2 = -1;
    if(b > max1) max1 = b;
    if(c > max1) max1 = c;
    if(d > max1) max1 = d;
    
    if(a < max1 && (max2 == -1 || a > max2)) max2 = a;
    if(b < max1 && (max2 == -1 || b > max2)) max2 = b;
    if(c < max1 && (max2 == -1 || c > max2)) max2 = c;
    if(d < max1 && (max2 == -1 || d > max2)) max2 = d;
    cout << max2;
    return 0;
    
}

/*
#include <iostream>
using namespace std;

#define nt int
#define nhap cin
#define xuat cout
#define kt return 0

nt main(){
    int a,b,c,d;
    nhap >> a >> b >> c >> d;
    nt max1 = a;
    if(b > max1) max1 = b;
    if(c > max1) max1 = c;
    if(d > max1) max1 = d;
    nt max2 = -999999;
    if(a > max2 && a < max1) max2 = a;
    if(b > max2 && b < max1) max2 = b;
    if(c > max2 && c < max1) max2 = c;
    if(d > max2 && d < max1) max2 = d;
    if(max2 == -999999) cout <<"-1";
    else cout << max2;
    kt;
}
*/

/*
#include <iostream>
#include <algorithm>
using namespace std;
int main(){
    int arr[4];
    cin >> arr[0] >> arr[1] >> arr[2] >> arr[3];
    
    sort(arr, arr + 4);
    
    // Tìm số lớn thứ nhì (khác số lớn nhất)
    for(int i = 2; i >= 0; i--) {
        if(arr[i] != arr[3]) {
            cout << arr[i];
            return 0;
        }
    }
    cout << -1;
    return 0;
}
*/