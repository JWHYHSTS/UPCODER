/*
Cho hai số nguyên dương x và y lần lượt là chỉ số một tháng và một năm. Hãy cho biết số ngày của tháng trong năm đó.

Input:

Gồm hai dòng, dòng thứ nhất gồm số nguyên dương x và dòng thứ hai gồm số nguyên dương y (x ≤ 12, y ≤ 3000).

Output:

In ra số ngày của tháng x trong năm y.

Ví dụ:

Input
1
2020
Output
31

Ví dụ 2:

Input
2
2024
Output
29

*/

#include <iostream>
using namespace std;
int main(){
    int x, y;
    cin >> x >> y;
    int ngay;
    switch(x){
        case 1: case 3: case 5: case 7: case 8: case 10: case 12:
            ngay = 31;
            break;
        case 4: case 6: case 9: case 11:
            ngay = 30;
            break;
        case 2:
            if(y % 400 == 0 || (y % 4 == 0 && y % 100 != 0)){
                ngay = 29;
            }
            else ngay = 28;
            break;
        default: 
            ngay = 0;
            break;
    }
    cout << ngay;
    return 0;
}