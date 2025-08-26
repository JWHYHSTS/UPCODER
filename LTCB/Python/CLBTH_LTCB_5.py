'''
Cho số nguyên n. Tính n! = 1 × 2 × 3 × 4 × … × n.

Input:

Gồm một số nguyên n duy nhất (n ≤ 20).

Output:

Giá trị của n!

Lưu ý: 0! = 1

Ví dụ:
Input
5
Output
120

'''
n = int(input().strip())
result = 1
for i in range(1, n + 1):
    result *= i
print(result)