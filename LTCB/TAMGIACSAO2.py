'''
TAM GIÁC SAO VUÔNG CÂN

Cho hình như sau:

*
**
***



Hình trên là 1 tam giác vuông cân được tạo từ các ký tự *.

Yêu cầu rất đơn giản, cho trước số ngôi sao, hãy xác định xem có thể xếp chúng thành một tam giác vuông cân được hay không.

 

Input

Một dòng chứa số nguyên N (1 <= N <= 10^18) là số ngôi sao.

 

Output

Một dòng chứa kết quả, nếu các ngôi sao có thể tạo thành tam giác vuông cân, in ra YES, ngược lại in ra NO

 

Ví dụ

input

3

output

YES

Giải thích:

Với n = 3, bạn có thể xếp được hình:

*

**

 

input

6

output

YES

Giải thích:

Với n = 6, bạn có thể xếp được hình:

*

**

***

 

input

5

output

NO

'''
n = int(input())
import math

x = 2 * n
k = int((math.isqrt(1 + 4 * x) - 1) // 2)
if k * (k + 1) // 2 == n:
    print("YES")
else:
    print("NO")