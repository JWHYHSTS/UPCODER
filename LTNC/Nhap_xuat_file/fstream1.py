'''
Nhập vào 2 số nguyên a và b.
yêu cầu xuất ra tổng của 2 số a và b

Dữ liệu vào từ file văn bản: input.txt gồm 2 số nguyên
Dữ liệu ra màn hình tổng 2 số nguyên đó

Ví dụ:

Input
2 3
Output
5

'''

with open("input.txt", "r") as f:
    a, b = map(int, f.read().split())

print(a + b)



