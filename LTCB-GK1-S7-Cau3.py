'''
Câu 3: (3đ)

Tính tổng các số nguyên tố trong phạm vi từ 1 đến n với n do người dùng nhập.

Input:

Nhập số nguyên n > 1.

Output:

In ra màn hình biểu thức tính tổng các số nguyên tố <=n

Ví dụ:
Input
10
1
Output
Tong cac so nguyen to <= 10 la:
2 + 3 + 5 + 7 = 17
NO
'''

import sys
def is_prime(x: int) -> bool:
    if x < 2: return False
    if x == 2: return True
    if x % 2 == 0: return False
    r = int(x ** 0.5)
    for i in range(3, r + 1, 2):
        if x % i == 0:
            return False
    return True

nums = list(map(int, sys.stdin.read().strip().split()))
for n in nums:
    if n <= 1:
        print("NO")
        continue
    primes = [p for p in range(2, n + 1) if is_prime(p)]
    if not primes:
        print("NO")
        continue
    total = sum(primes)
    print(f"Tong cac so nguyen to <= {n} la:")
    expr = " + ".join(map(str, primes))
    print(f"{expr} = {total}")