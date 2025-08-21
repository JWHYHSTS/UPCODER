'''
Viết chương trình in ra màn hình hình chữ nhật sao rỗng với độ dài 2 cạnh nhập vào từ bàn phím.

Input: 2 số nguyên dương a, b.
Output: hình chữ nhật ngôi sao rỗng giữa tương ứng độ dài 2 cạnh.

Ví dụ:

Input:
3 5

Output:
*****
*   *
*****

Input:
5 8

Output:
********
*      *
*      *
*      *
********

Dữ liệu nhập đảm bảo vẽ được hình chữ nhật rỗng.

Lưu ý: 
Xuất chính xác từng ký tự. Không xuất dư hoặc thiếu khoảng trắng, không xuất dư endl dòng cuối cùng.

'''
a, b = map(int, input().split())
for i in range(a):
    if i == 0 or i == a - 1:
        line = '*' * b
    else:
        line = '*' + ' ' * (b - 2) + '*'
    if i == a - 1:
        print(line, end="")
    else:
        print(line)