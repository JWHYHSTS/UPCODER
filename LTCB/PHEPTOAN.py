'''
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
'''

a, b = map(int, input().split())
c = input()
if c == "+":
    print(f"{a}+{b}={a+b}")
elif c == "-":
    print(f"{a}-{b}={a-b}")
elif c == "*":
    print(f"{a}*{b}={a*b}")
elif c == "%":
    print(f"{a}%{b}={a%b}")
