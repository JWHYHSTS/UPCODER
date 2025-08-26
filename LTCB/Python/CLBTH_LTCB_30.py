'''
Nhập vào từ bàn phím một số nguyên dương n. Hãy tìm và in ra màn hình chữ số lớn nhất của số n.
Input:
Một số nguyên dương n.
Output:
Đáp án của bài toán.
Ví dụ:

Input
70128
Output
8

'''
n = int(input().strip())
max_digit = 0
while n > 0:
    max_digit = max(max_digit, n % 10)
    n //= 10
print(max_digit)