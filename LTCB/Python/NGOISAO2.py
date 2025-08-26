'''
Viết chương trình in ra màn hình hình chữ nhật sao với độ dài 2 cạnh nhập vào từ bàn phím.

Input: 2 số nguyên dương a, b.
Output: hình chữ nhật ngôi sao tương ứng độ dài 2 cạnh.

Ví dụ:

Input:
3 5

Output:
*****
*****
*****
Lưu ý: 

Xuất chính xác từng ký tự. Không xuất dư hoặc thiếu khoảng trắng, không xuất dư endl dòng cuối cùng.
'''

a, b = map(int, input().split())
for i in range(a):
    if i < a - 1:
        print('*' * b)
    else:
        print('*' * b, end="")
