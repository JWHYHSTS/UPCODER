'''
Viết chương trình sử dụng hàm đệ quy tính số hạng thứ N của dãy Fibonacci.
Biết rằng, dãy Fibonacci được định nghĩa bởi công thức:

Fibo(n) = 1 khi n = {1,2}
Fibo(n) = Fibo(n - 1) + Fibo(n - 2) khi n>2

Input: Số nguyên dương n (n <= 100)

Output: Số Fibonacci thứ n.

Ví dụ:

Input
10
Output
55



Giải thích: Một vài số hạng đầu tiên của dãy Fibonacci là: 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, ...

'''

import sys
data=sys.stdin.read().strip().split()
if not data: sys.exit()
n=int(data[0])

def fib(k):
    if k<=2: return 1
    return fib(k-1)+fib(k-2)

print(fib(n))