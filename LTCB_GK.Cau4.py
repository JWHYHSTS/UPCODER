'''
Nhập vào một số nguyên trong phạm vi từ 50…59. Hiển thị cách đọc số đó.

Input
50
55
53
Output
Nam muoi
Nam muoi lam
Nam muoi ba
'''

import sys

units = {
    0: "Nam muoi",  # 50
    1: "Nam muoi mot",
    2: "Nam muoi hai",
    3: "Nam muoi ba",
    4: "Nam muoi bon",
    5: "Nam muoi lam",
    6: "Nam muoi sau",
    7: "Nam muoi bay",
    8: "Nam muoi tam",
    9: "Nam muoi chin"
}

for token in sys.stdin.read().strip().split():
    n = int(token)
    if 50 <= n <= 59:
        print(units[n - 50])
    else:
        print("NO")