'''
Nhập vào 2 số nguyên N và M, yêu cầu tính tổng chữ số cuối cùng của  N và của M.
(0<= N,M <=12345670)

ví dụ:
input:
123
456

output
9
'''

a, b = map(int, input().split())
print((a % 10 + b % 10) % 10)