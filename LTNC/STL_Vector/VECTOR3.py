'''
Sử dụng container vector, anh/chị hãy viết chương trình đọc vào các số nguyên, sau đó loại bỏ các số chính phương trong vector rồi xuất ra các số chẵn theo thứ tự tăng dần.

Ví dụ:

Input
7 6 5 4 3 2 1
Output
2 6

'''

import math

def is_perfect_square(n):
    return int(math.sqrt(n))**2 == n
nums = list(map(int, input().split()))
filtered = [x for x in nums if not is_perfect_square(x)]
even_numbers = [x for x in filtered if x % 2 == 0]
even_numbers.sort()
print(' '.join(map(str, even_numbers)))