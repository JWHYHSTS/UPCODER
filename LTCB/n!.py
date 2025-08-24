'''
Nhập vào 1 số nguyên n, xuất ra n!

ví dụ:

input:
3

output:
6
'''
n = int(input())
def gt(n):
    if n == 0:
        return 1
    else:
        return n * gt(n - 1)
print(gt(n))

# Cách 2:
'''
n = int(input())
def gt_iter(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

print(gt_iter(n))
'''