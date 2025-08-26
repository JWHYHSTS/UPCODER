/*
nhập vào 2 số nguyên và 1 phép toán. Yêu cầu thực hiện phép toán (là 1 trong 4 phép toán: +,-,*,%)

Input:

- Dòng 1: nhập vào 2 số nguyên A, B

- Dòng 2: Nhập vào 1 phép toán

Output:

-Biểu thức thực hiện phép toán.



Ví dụ:

Input:

1 2

+

Output:

1+2=3
*/
#include <iostream>
using namespace std;

int main(){
    int a, b;
    char c;
    cin >> a >> b >> c;
    if(c == '+') {
        cout << a << "+" << b << "=" << a + b;
    } else if(c == '-'){
        cout << a << "-" << b << "=" << a - b;
    } else if(c == '*'){
        cout << a << "*" << b << "=" << a * b;
    } else cout << a << "%" << b << "=" << a % b;
    return 0;
}

/*
Cách 2: 
switch(c) {
    case '+':
        cout << a << "+" << b << "=" << a + b;
        break;
    case '-':
        cout << a << "-" << b << "=" << a - b;
        break;
    case '*':
        cout << a << "*" << b << "=" << a * b;
        break;
    case '%':
        cout << a << "%" << b << "=" << a % b;
        break;
    default:
        cout << "Phép toán không hợp lệ";
}
*/