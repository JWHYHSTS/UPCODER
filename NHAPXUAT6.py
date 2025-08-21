'''
Input:
Dòng 1: chứa 1 ký tự 
Dòng 2: chưa 1 ký tự 
Output:
Xuất tổng nguyên của 2 ký tự trong input ra màn hình (dựa vào hệ 10 của ký tự trong bảng mã ascii)
Ví dụ:

Input	
A
B
Output
131
'''

a = input()
b = input()
print(ord(a) + ord(b))
