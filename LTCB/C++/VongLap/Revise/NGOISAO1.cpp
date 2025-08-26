/*
Viết chương trình in ra màn hình ngôi sao (với chiều cao h nhập từ bàn phím)

ví dụ:

input:

3

output

*
**
***
*/

#include <iostream>
using namespace std;
int main(){
    int h;
    cin >> h;
    for(int i = 1; i <= h; i++){
        for(int j = 1; j <= i; j++){
            cout << "*";
        }
        cout << endl;
    }
    return 0;
}