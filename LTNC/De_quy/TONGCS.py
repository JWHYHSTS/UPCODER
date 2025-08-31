'''
Viết một chương trình đệ quy tính tổng các chữ số của số N cho trước   (N<= 123456789)

Ví dụ: 

Input: 123 

Ouput: 6 

(vì : 1+2+3 =6)

'''

import sys
data=sys.stdin.read().strip()
if not data: sys.exit()
n=int(data)
def sum_digits(x):
    if x<10: return x
    return x%10 + sum_digits(x//10)
print(sum_digits(n))