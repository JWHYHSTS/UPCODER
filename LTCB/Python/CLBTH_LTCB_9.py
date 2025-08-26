'''
Cho một số nguyên dương n, hãy phân tích n thành tích các thừa số nguyên tố.

Input:

Gồm một số nguyên dương n duy nhất (2 ≤ n ≤ 106).

Output:

Gồm một dòng in ra các thừa số nguyên tố (sau khi phân tích n) theo thứ tự từ bé đến lớn.

Ví dụ:
Input
60
Output
2 2 3 5
'''
n = int(input().strip())
factors = []
x = n
d = 2
while d * d <= x:
    while x % d == 0:
        factors.append(str(d))
        x //= d
    d += 1 if d == 2 else 2  
if x > 1:
    factors.append(str(x))
print(" ".join(factors))