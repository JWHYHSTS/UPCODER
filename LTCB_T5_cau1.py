'''
Cho 2 số nguyên dương m và n

Yêu cầu: 

Xuất tất cả các số nguyên tố có trong khoảng [m,n]

Nếu không có thì xuất -1


Ví dụ: 
Input: 3 9
Output: 3 5 7
'''
def snt(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
a, b = map(int, input().split())
found = False
for i in range(a, b + 1):
    if snt(i):
        print(i, end=' ')
        found = True
if not found:
    print(-1)
    
''' Cách 2:
def is_prime(x):
    if x < 2:
        return False
    if x == 2:
        return True
    if x % 2 == 0:
        return False
    r = int(x ** 0.5)
    for i in range(3, r + 1, 2):
        if x % i == 0:
            return False
    return True

m, n = map(int, input().split())
primes = [str(i) for i in range(m, n + 1) if is_prime(i)]
if primes:
    print(" ".join(primes))
else:
    print(-1)
'''