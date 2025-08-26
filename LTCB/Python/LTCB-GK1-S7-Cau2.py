'''
Câu 2: (2đ)

Nhập vào một số nguyên trong phạm vi từ 50..59. Hiển thị cách đọc số đó.
Input: 
Nhập số nguyên n (50<= n <=59)
Ouput: 
Cách đọc số n
Ví dụ:

Input
55
54
Output
Nam muoi lam
Nam muoi bon
'''
import sys

def read_50s(n: int) -> str:
    if not (50 <= n <= 59):
        return "NO"
    if n == 50:
        return "Nam muoi"
    units_map = {
        1: "mot",
        2: "hai",
        3: "ba",
        4: "bon",
        5: "lam",
        6: "sau",
        7: "bay",
        8: "tam",
        9: "chin"
    }
    return "Nam muoi " + units_map[n % 10]

nums = list(map(int, sys.stdin.read().strip().split()))
for n in nums:
    print(read_50s(n))