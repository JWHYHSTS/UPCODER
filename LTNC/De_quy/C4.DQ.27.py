'''
Viết chương trình sử dụng hàm đệ quy tính LASTNUM của một số nguyên dương.
Biết rằng: Một LASTNUM của một số được xác định bằng cách lấy tổng các chữ số của số đó, sau đó lại tiếp tục tính tổng các chữ số của số mới tạo ra cho đến khi chỉ còn một chữ số duy nhất.

Input: Số nguyên dương n (n <= 10^18).
Output: Số duy nhất là LASTNUM của số n.

Ví dụ:

Input
789
Output
6


Giải thích: Các số được tạo ra lần lượt là: 789 → 24 → 6 .

'''


import sys
data = sys.stdin.read().strip().split()
if not data: sys.exit()
n = int(data[0])

def digit_sum(x):
    if x < 10:
        return x
    return x % 10 + digit_sum(x // 10)

def lnum(x):
    if x < 10:
        return x
    return lnum(digit_sum(x))

print(lnum(n))