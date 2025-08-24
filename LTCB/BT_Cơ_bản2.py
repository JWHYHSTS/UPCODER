'''
Cho 2 số nguyên dương a, b < 100, viết hàm tìm UCLN và BCNN.

VD Input: 9 12

Output: 3 36 

'''
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a
def lcm(a, b):
    return a * b // gcd(a, b)

a, b = map(int, input().split())
print(gcd(a, b), lcm(a, b))