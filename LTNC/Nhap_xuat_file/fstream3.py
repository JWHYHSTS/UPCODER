'''
Nhập vào 2 số nguyên a và b.
yêu cầu xuất ra tổng của 2 số a và b

Dữ liệu vào từ bàn phím (nhập chuẩn) gồm 2 số nguyên
Dữ liệu ra file văn bản out.txt tổng 2 số nguyên đó
Ví dụ:

Input
2 3
Output
5

'''

a, b = map(int, input().split())

with open("out.txt", "w") as f:
    f.write(str(a + b))