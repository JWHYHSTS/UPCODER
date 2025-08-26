/*
Biết rằng giá tiền điện được tính như sau:

- từ KW thứ 1 đến 50 giá 1678 đồng/KW.

- từ KW thứ 51 đến 100 giá 1734 đồng/KW.

- từ KW thứ 101 đến 200 giá 2014 đồng/KW.

- từ KW thứ 201 đến 300 giá 2536 đồng/KW.

- từ KW thứ 301 đến 400 giá 2834 đồng/KW.

- từ KW thứ 401 trở đi giá 2937 đồng/KW.

Cho một số nguyên x là số KW điện tiêu thụ của một hộ gia đình. Tính số tiền điện mà hộ gia đình đó phải trả.

Input:

Gồm một số nguyên dương x duy nhất.

Output:

Số tiền phải trả theo đơn vị đồng.

Ví dụ:


Input
10
Output
16780
*/

#include <iostream>
using namespace std;
int main(){
    int x;
    cin >> x;
    int tong = 0;
    if(x <= 50){
        tong = x * 1678;
    }else if(x <= 100){
        tong = 50 * 1678 + (x - 50) * 1734;
    }else if(x <= 200){
        tong = 50 * 1678 + 50 * 1734 + (x - 100) * 2014;
    }else if(x <= 300){
        tong = 50 * 1678 + 50 * 1734 + 100 * 2014 + (x - 200) * 2536;
    }else if(x <= 400){
        tong = 50 * 1678 + 50 * 1734 + 100 * 2014 + 100 * 2536 + (x - 300) * 2834;
    }else{
        tong = 50 * 1678 + 50 * 1734 + 100 * 2014 + 100 * 2536 + 100 * 2834 + (x - 400) * 2937;
    }
    cout << tong;
    return 0;
}