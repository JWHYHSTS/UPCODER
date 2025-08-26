'''
Năm 2024 là thế kỷ 21. Nhập vào số nguyên dương n, bạn hãy xác định xem năm n thuộc thế kỷ thứ mấy.

Input:

Một số nguyên n duy nhất.

Output:

Một số nguyên duy nhất là thế kỷ chứa năm n.

Ví dụ:
Input
2024
Output
21
'''
n = int(input().strip())
if n % 100 == 0:
    print(n // 100)
else:
    print(n // 100 + 1)