'''
Input:
- Dòng 1: Nhập vào N là số lượng phần tử của mảng
- Dòng 2: N số nguyên (mỗi số cách 1 khoảng trắng)

Ouput:
- Dòng 1: xuất các số chính phương của dãy
- Dòng 2: xuất các số nguyên tố của dãy

Ví dụ:
input
4
1 2 3 4
output
1 4
2 3

'''
import math

def is_square(n):
    if n < 0:
        return False
    root = int(math.isqrt(n))
    return root * root == n

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

n = int(input())
mang = list(map(int, input().split()))
scp = [str(x) for x in mang if is_square(x)]
snt = [str(x) for x in mang if is_prime(x)]

print(" ".join(scp))
print(" ".join(snt))